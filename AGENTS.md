# Agent Instructions

This repository is a minimal AI-assisted defensive log-review experiment.

## Safety Rules

- Do not add code that uploads sample logs containing secrets, personal data, customer data, credentials, or regulated records.
- Do not commit API keys, `.env` files, or real incident logs.
- Keep hosted-model usage explicit; do not silently choose a default model.
- Treat model output as analyst assistance, not ground truth.

## Good Agent Tasks

- Add local redaction before hosted-model calls.
- Add structured JSON output for flagged lines.
- Add sample synthetic logs and tests.
- Add deterministic prefilters before the model call.
- Add local-model adapter scaffolding.

## Verification

```bash
python -m py_compile aiLogger.py
```
