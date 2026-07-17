## Nano GPT
An small LLM build from scratch for pedagogical reasons

## Setup

Requires Python 3.14.2 (see `.python-version`) and an NVIDIA GPU with CUDA 12.6 (torch is pinned to a `cu126` build).

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # macOS/Linux
pip install -r requirements.txt
```

If you don't have a CUDA 12.6 GPU, edit `requirements.txt` and drop the `+cu126` suffix from the `torch`/`torchvision` lines (they'll then install CPU-only builds from PyPI).