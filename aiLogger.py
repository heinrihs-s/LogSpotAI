# ailogger.py

import os
import argparse
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure you have your key in an environment variable

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
    Send the log lines to a language model in small chunks, 
    asking it to flag suspicious entries.
    """
    suspicious_lines = []
    
    # Process in chunks to avoid prompt length issues
    for i in range(0, len(log_lines), chunk_size):
        chunk = log_lines[i:i+chunk_size]
        prompt = (
            "You are a security analyst. "
            "Below are some log entries. Identify which ones look suspicious or anomalous:\n\n"
        )
        numbered_lines = "\n".join(f"{idx+1}. {line}" for idx, line in enumerate(chunk))
        prompt += numbered_lines
        prompt += "\n\nList suspicious line numbers along with a short reason.\n"

        response = openai.Completion.create(
            engine="text-davinci-003",  # or 'gpt-3.5-turbo' with ChatCompletion
            prompt=prompt,
            max_tokens=200,
            temperature=0
        )
        
        # Parse the response to find which line numbers are flagged
        flagged_data = response.choices[0].text.strip()
        # Very naive parsing: you could do something more structured
        for line in flagged_data.split('\n'):
            if line.strip() and any(char.isdigit() for char in line):
                # e.g. "1 - suspicious because..."
                line_num_str = line.split('-')[0].strip()
                try:
                    line_num = int(line_num_str)
                    # original index in full log_lines
                    suspicious_lines.append(chunk[line_num - 1])
                except ValueError:
                    pass

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
