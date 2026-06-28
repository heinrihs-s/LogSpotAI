# LogSpotAI

Small defensive log-review script that sends chunks of a local log file to an OpenAI model and prints the lines the model flags as suspicious.

This is intentionally a minimal experiment, not a SIEM, detector, or production incident-response system. It is useful as a readable baseline for AI-assisted triage workflows and prompt design.

Keywords: log analysis, security logs, AI-assisted triage, defensive security, OpenAI, Python.

## Safety And Privacy

- Review logs before sending them to any hosted model.
- Do not send secrets, personal data, customer data, credentials, or regulated records.
- Treat the output as analyst assistance, not a finding by itself.
- Validate suspicious lines manually.

## Requirements

- Python 3.10+
- OpenAI Python SDK
- `OPENAI_API_KEY`
- `OPENAI_MODEL`

Install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

```bash
export OPENAI_API_KEY="..."
export OPENAI_MODEL="your-model-name"
python aiLogger.py --logfile /path/to/logfile.log
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="..."
$env:OPENAI_MODEL="your-model-name"
python .\aiLogger.py --logfile .\sample.log
```

The script:

1. reads non-empty log lines,
2. batches them into small chunks,
3. asks the model for suspicious line numbers,
4. prints the original flagged lines for review.

## Limits

- No structured parser yet.
- No redaction layer yet.
- No deterministic detection rules.
- No guarantee that the model catches the important line.

For production work, pair model-assisted review with deterministic parsing, local redaction, SIEM rules, and human verification.

## Agent-Friendly Workflow

This repo includes `AGENTS.md` for Codex, Claude Code, and other coding agents. Good next tasks include local redaction, synthetic sample logs, structured JSON output, deterministic prefilters, and local-model adapters.

## License

MIT. See `LICENSE`.
