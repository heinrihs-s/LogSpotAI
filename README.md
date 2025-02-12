# LogSpotAI

A lightweight **AI-assisted log analysis tool** written in Python. LogSpotAI helps you detect suspicious or anomalous log entries using a large language model (LLM) or other AI methods. The entire project is kept minimal, with just one or two Python files, so it's easy to understand, modify, and extend.

## Features

- **Simple CLI**: Pass in your log file, get back suspicious lines.
- **AI-Powered**: Uses OpenAI's API (or switch to your preferred AI model).
- **Minimal**: Only one main Python script + this README + requirements.
- **Extendable**: You can adapt it for various log formats and different AI endpoints.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/heinrihs-s/LogSpotAI.git
cd LogSpotAI
```

### 2. Create a Virtual Environment

```bash
# On Linux/Mac
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Your OpenAI API Key

* Sign up or log in to OpenAI to get an API key
* Export the key as an environment variable:

```bash
# Linux/Mac
export OPENAI_API_KEY="your_secret_key"

# Windows (Command Prompt)
set OPENAI_API_KEY="your_secret_key"
```

Or create a `.env` file (if you add `python-dotenv` support) to store your key locally.

### 5. Usage

Basic usage:
```bash
python ailogger.py --logfile /path/to/your.log
```

Example with sample log:
```bash
python ailogger.py --logfile sample.log
```

* The script reads your logs, batches them, and queries the AI model to identify potentially suspicious lines
* Suspicious lines are then printed out for review


## Customization

* **Local Models**: If you prefer not to use the OpenAI API, switch to a local anomaly-detection model (e.g., scikit-learn's `IsolationForest` or a small transformer)
* **Thresholding**: For local models, you can tweak detection thresholds to adjust sensitivity
* **Log Parsing**: Enhance the `parse_logfile` function to handle different log formats (JSON logs, Apache logs, etc.)
* **Report Generation**: Output results to a separate file, or incorporate visualizations if you want

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a PR or issue on the GitHub repository.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software as you see fit, but attribution is appreciated.

---

### Additional Tips

1. If you want to keep everything in just *one* Python file, you can place your CLI and AI logic all in ailogger.py and skip any separate scripts
2. Add a sample log file (`sample.log`) and demonstrate how the script flags suspicious lines
3. Consider adding a small test script or a test folder with example inputs and outputs

Happy Logging with **LogSpotAI**!
