#

import os
import json
import torch
import torch.distributed as dist
from typing import Any, Dict, List, Optional, Type, Union

from pydantic import BaseModel, Field

from llama_stack.apis.models.models import ModelType
from llama_stack.providers.datatypes import (
    Model,
    ModelsProtocol,
    CompletionRequest,
    CompletionResponse,
    TokenizationRequest,
    TokenizationResponse,
)
from llama_stack.providers.protocols import InferenceProtocol
from llama_stack.providers.utils.inference.model_registry import (
    ProviderModelEntry,
    ModelRegistryHelper,
)

MODEL_ENTRIES = [
    ProviderModelEntry(
        provider_model_id="deepseek-v3",
        aliases=["deepseek-v3-chat", "deepseek-v3-671b"],
        llama_model="deepseek-v3",
        model_type=ModelType.llm,
        metadata={
            "size": "671B",
            "context_length": 128000,
            "precision": "fp8",
        },
    ),
]

model_registry = ModelRegistryHelper(MODEL_ENTRIES)

class DeepSeekV3Provider(ModelsProtocol, InferenceProtocol):
    def __init__(self, **kwargs):
        self.model_config_path = os.path.join(
            os.environ.get("DEEPSEEK_V3_PATH", os.path.expanduser("~/repos/DeepSeek-V3")),
            "inference/configs/config_671B.json"
        )
        
    async def list_models(self, model_type: Optional[ModelType] = None) -> List[Model]:
        models = []
        for entry in MODEL_ENTRIES:
            if model_type is None or entry.model_type == model_type:
                models.append(
                    Model(
                        model_id=entry.provider_model_id,
                        provider_id="deepseek_v3",
                        provider_resource_id=entry.provider_model_id,
                        model_type=entry.model_type,
                        metadata={
                            "llama_model": entry.llama_model,
                            **entry.metadata,
                        },
                    )
                )
        return models

    async def get_model(self, model_id: str) -> Model:
        provider_model_id = model_registry.get_provider_model_id(model_id)
        if provider_model_id is None:
            raise ValueError(f"Model '{model_id}' not found")
        
        for model in await self.list_models():
            if model.provider_resource_id == provider_model_id:
                return model
        
        raise ValueError(f"Model '{model_id}' not found")

    async def register_model(self, model: Model) -> Model:
        return await model_registry.register_model(model)

    async def tokenize(self, request: TokenizationRequest) -> TokenizationResponse:
        raise NotImplementedError("Tokenization not yet implemented for DeepSeek-V3")
        
    async def complete(self, request: CompletionRequest) -> CompletionResponse:
        raise NotImplementedError("Completion not yet implemented for DeepSeek-V3")

def get_provider(**kwargs) -> DeepSeekV3Provider:
    return DeepSeekV3Provider(**kwargs)
