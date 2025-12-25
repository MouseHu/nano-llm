# Nano LLM

In this project, I will try to build a LLM from scratch with pytorch, including : tokenizer; pretraining; sft; rl; vllm;

I will try to use a distributed dataloader/trainer to better understand the training mechanism of Megatron-LM. To do this, it seems that I need more than one gpus. I will first verify single GPU setting and then rent a GPU cluster on the cloud. I expect ~10000 cost for a reasonably well LLM (e.g., 1.5B with 300B tokens)


Major project I am refering to includes: nano-GPT, nano-VLLM, minimind and nano chat.

## Key Points for this project

- Have experiment to write production level code: pytest, pyproject.toml, ruff, pre-commit etc.
- Understanding the whole lifecycle of LLMs, (for example, I never know there is pre-tokenization splitting if I haven't implemented one)
- Have a simple experiment interface to do ablations on architectures/data/rope embeddings/optimizers/vlm/omni on my own.


## How it contribute to my long term goal

- Understanding of production level code: key to lead a project;
- Understanding of LLMs: key to improve it, be able to do research on it; (e.g., diffusion LM?)
- Understanding of infra: vllm etc.
- Talk is cheap, show me the code.
