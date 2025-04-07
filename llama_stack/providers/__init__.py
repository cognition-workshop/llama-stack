# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Dict, Callable, Any

from llama_stack.providers import deepseek_v3

PROVIDERS: Dict[str, Callable[..., Any]] = {
    "deepseek_v3": deepseek_v3.get_provider,
}
