#

import os
import argparse
import json
import torch
import torch.distributed as dist

def setup_distributed_inference(num_nodes=2, gpus_per_node=8, model_path=None):
    """
    Set up distributed inference for DeepSeek-V3 using SGLang.
    
    Args:
        num_nodes: Number of nodes to use
        gpus_per_node: Number of GPUs per node
        model_path: Path to the model weights
    """
    world_size = num_nodes * gpus_per_node
    
    if model_path is None:
        model_path = os.path.expanduser("~/repos/DeepSeek-V3")
    
    print(f"Setting up distributed inference for DeepSeek-V3")
    print(f"Number of nodes: {num_nodes}")
    print(f"GPUs per node: {gpus_per_node}")
    print(f"Total world size: {world_size}")
    print(f"Model path: {model_path}")
    
    
    return {
        "model_path": model_path,
        "num_nodes": num_nodes,
        "gpus_per_node": gpus_per_node,
        "world_size": world_size,
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up distributed inference for DeepSeek-V3")
    parser.add_argument("--num-nodes", type=int, default=2, help="Number of nodes")
    parser.add_argument("--gpus-per-node", type=int, default=8, help="Number of GPUs per node")
    parser.add_argument("--model-path", type=str, default=None, help="Path to model weights")
    
    args = parser.parse_args()
    setup_distributed_inference(args.num_nodes, args.gpus_per_node, args.model_path)
