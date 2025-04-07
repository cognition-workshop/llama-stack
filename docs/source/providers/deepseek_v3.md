# DeepSeek-V3 Provider

This document describes how to use the DeepSeek-V3 provider for running evaluations with Llama Stack.

## Overview

DeepSeek-V3 is a large Mixture-of-Experts (MoE) model with 671B total parameters (37B activated). This provider integrates DeepSeek-V3 with Llama Stack for evaluation purposes, particularly for running the GPQA benchmark.

## Requirements

- DeepSeek-V3 repository: `https://github.com/deepseek-ai/DeepSeek-V3`
- SGLang (v0.4.1 or later): `pip install sglang==0.4.1`
- Hardware: Minimum of 2 nodes with 8 GPUs each (or equivalent)
- Model weights: FP8 weights for DeepSeek-V3 from Hugging Face

## Setting Up

1. Clone the DeepSeek-V3 repository:
   ```bash
   git clone https://github.com/deepseek-ai/DeepSeek-V3 ~/repos/DeepSeek-V3
   ```

2. Download the model weights:
   ```bash
   # Instructions for downloading model weights
   ```

3. Set environment variables:
   ```bash
   export DEEPSEEK_V3_PATH=~/repos/DeepSeek-V3
   ```

## Running GPQA Benchmark

To run the GPQA benchmark evaluation on DeepSeek-V3:

```bash
cd ~/repos/llama-stack
python scripts/run_deepseek_v3_gpqa.py --num-nodes 2 --gpus-per-node 8
```

This will set up distributed inference for DeepSeek-V3, start the Llama Stack server with the open-benchmark template, and run the GPQA benchmark evaluation.

## Results

The evaluation results will be saved to `./evaluation-results/deepseek-v3-gpqa` by default. You can specify a different output directory using the `--output-dir` option.

## Troubleshooting

If you encounter issues with distributed inference, make sure:

1. All nodes can communicate with each other
2. The same version of SGLang is installed on all nodes
3. The model weights are accessible from all nodes
