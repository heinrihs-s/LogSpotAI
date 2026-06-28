import os
import argparse
import re

from openai import OpenAI


def parse_logfile(log_path):
    """
    Basic log parsing: read lines, return as a list of strings.
    Add any extra parsing or filtering logic here.
    """
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]

def analyze_logs_with_ai(log_lines, chunk_size=30):
    """
    Send log lines to a model in small chunks and ask it to flag suspicious entries.
    """
    model = os.getenv("OPENAI_MODEL")
    if not model:
        raise RuntimeError("Set OPENAI_MODEL to the model you want to use.")

    client = OpenAI()
    suspicious_lines = []

    for i in range(0, len(log_lines), chunk_size):
        chunk = log_lines[i:i+chunk_size]
        numbered_lines = "\n".join(
            f"{idx+1}. {line}" for idx, line in enumerate(chunk)
        )

        response = client.responses.create(
            model=model,
            instructions=(
                "You are a defensive security analyst. Review log lines and flag "
                "only entries that look suspicious or anomalous. Return one finding "
                "per line as '<line_number> - <short reason>'. Return 'none' when "
                "nothing in the chunk is suspicious."
            ),
            input=numbered_lines,
            temperature=0,
        )

        flagged_data = response.output_text.strip()
        for line in flagged_data.splitlines():
            match = re.match(r"^\s*(\d+)\s*[-:]", line)
            if match:
                line_num = int(match.group(1))
                if 1 <= line_num <= len(chunk):
                    suspicious_lines.append(chunk[line_num - 1])

    return suspicious_lines

def main():
    parser = argparse.ArgumentParser(description="AI-Assisted Log Analyzer")
    parser.add_argument("--logfile", required=True, help="Path to the log file")
    args = parser.parse_args()

    # Step 1: Parse the logs
    logs = parse_logfile(args.logfile)

    # Step 2: Analyze logs with AI
    suspicious = analyze_logs_with_ai(logs)

    # Step 3: Report
    if suspicious:
        print("Suspicious lines found:")
        for s_line in suspicious:
            print(f"- {s_line}")
    else:
        print("No suspicious lines detected.")

if __name__ == "__main__":
    main()
