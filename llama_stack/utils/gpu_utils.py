#

import logging
from typing import List

from pynvml import (
    nvmlInit,
    nvmlDeviceGetCount,
    nvmlDeviceGetHandleByIndex,
    nvmlDeviceGetName,
    nvmlDeviceGetMemoryInfo,
    nvmlDeviceGetUtilizationRates,
    nvmlShutdown,
)

from llama_stack.apis.inspect.inspect import GPUInfo

logger = logging.getLogger(__name__)


def get_gpu_info() -> List[GPUInfo]:
    """
    Get information about available GPUs including memory usage and utilization.
    
    Returns:
        List[GPUInfo]: List of GPU information objects, empty list if no GPUs or error
    """
    try:
        nvmlInit()
        device_count = nvmlDeviceGetCount()
        result = []
        
        for i in range(device_count):
            handle = nvmlDeviceGetHandleByIndex(i)
            name = nvmlDeviceGetName(handle)
            memory = nvmlDeviceGetMemoryInfo(handle)
            utilization = nvmlDeviceGetUtilizationRates(handle)
            
            gpu_info = GPUInfo(
                index=i,
                name=name,
                memory_used=memory.used // (1024 * 1024),  # Convert to MB
                memory_total=memory.total // (1024 * 1024),  # Convert to MB
                utilization=utilization.gpu
            )
            result.append(gpu_info)
            
        nvmlShutdown()
        return result
    except Exception as e:
        logger.warning(f"Failed to get GPU info: {e}")
        return []
