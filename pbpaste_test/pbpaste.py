#!/usr/bin/env python3
"""
pbpaste v0 - A simple script to emulate the macOS pbpaste command
"""
import subprocess
import sys

def get_clipboard_content():
    """Get content from the system clipboard"""
    try:
        # On macOS
        process = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        clipboard_content, _ = process.communicate()
        return clipboard_content.decode('utf-8')
    except Exception as e:
        print(f"Error accessing clipboard: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    content = get_clipboard_content()
    if content:
        print(content, end="")
    else:
        sys.exit(1)