# Poandy

Simple Python wrapper for Oanda (https://developer.oanda.com/rest-live-v20/introduction/).

## Setup

I'm using Python 3.8.5 on Windows Git Bash.

    cd poandy
    python -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

## Linter

Use flake8 without line length limit.
If using vscode, include the following in settings.json

    "python.linting.flake8Args": ["--max-line-length=200"]

## Test

    pytest
