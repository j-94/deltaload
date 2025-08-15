# pbpaste v0

A simple Python script that emulates the macOS `pbpaste` command, retrieving content from the system clipboard.

## Usage

```
./pbpaste.py
```

## Requirements

- Python 3
- On macOS, requires the built-in `pbpaste` command

## How it works

This script simply wraps the system's clipboard access command (currently using macOS' `pbpaste`) and outputs the content to stdout, making it easy to pipe into other commands or redirect to files.

## Future Improvements

- Cross-platform support (Windows, Linux)
- Support for different content types (text, image, etc.)
- Command-line options for formatting