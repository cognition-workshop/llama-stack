#

import os
import argparse
import subprocess
import json

from scripts.setup_deepseek_v3 import setup_distributed_inference

def run_gpqa_benchmark(num_nodes=2, gpus_per_node=8, model_path=None, output_dir=None):
    """
    Run the GPQA benchmark evaluation on DeepSeek-V3.
    
    Args:
        num_nodes: Number of nodes to use
        gpus_per_node: Number of GPUs per node
        model_path: Path to the model weights
        output_dir: Directory to save evaluation results
    """
    config = setup_distributed_inference(num_nodes, gpus_per_node, model_path)
    
    if output_dir is None:
        output_dir = "./evaluation-results/deepseek-v3-gpqa"
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("Starting Llama Stack server with open-benchmark template...")
    server_cmd = "llama stack run llama_stack/templates/open-benchmark/run.yaml"
    
    
    print("Running GPQA benchmark evaluation...")
    benchmark_cmd = f"llama-stack-client eval run-benchmark meta-reference-gpqa-cot --model_id deepseek-v3 --output_dir {output_dir}"
    
    print(f"Would execute: {benchmark_cmd}")
    
    print(f"Evaluation results will be saved to: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run GPQA benchmark evaluation on DeepSeek-V3")
    parser.add_argument("--num-nodes", type=int, default=2, help="Number of nodes")
    parser.add_argument("--gpus-per-node", type=int, default=8, help="Number of GPUs per node")
    parser.add_argument("--model-path", type=str, default=None, help="Path to model weights")
    parser.add_argument("--output-dir", type=str, default=None, help="Directory to save evaluation results")
    
    args = parser.parse_args()
    run_gpqa_benchmark(args.num_nodes, args.gpus_per_node, args.model_path, args.output_dir)
