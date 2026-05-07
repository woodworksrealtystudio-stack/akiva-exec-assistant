#!/usr/bin/env python3
"""
Perplexity research tool.
Usage: python3 tools/research.py "your query here"
"""

import sys
import os
import json
import urllib.request
import urllib.error


def search(query: str) -> None:
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        print("Error: PERPLEXITY_API_KEY not set in environment.")
        sys.exit(1)

    payload = json.dumps({
        "model": "llama-3.1-sonar-large-128k-online",
        "messages": [{"role": "user", "content": query}],
        "max_tokens": 1024,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.perplexity.ai/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(data["choices"][0]["message"]["content"])
    except urllib.error.HTTPError as e:
        print(f"API error {e.code}: {e.read().decode()}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/research.py \"your query here\"")
        sys.exit(1)
    query = " ".join(sys.argv[1:])
    search(query)
