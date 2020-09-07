# Poandy

Simple Python wrapper for Oanda (https://developer.oanda.com/rest-live-v20/introduction/).

## Setup

I'm using Python 3.8.5 on Windows Git Bash. Commands may differ.

    git clone ..
    cd poandy
    # create a file called "secrets.json". It should contain your oanda api key. E.g.
    {
        "token": "7851c27f3bb2bc0f39g3c6d6a3c6b42509e-4015643c1a6ca4651b0c6bd836bc8b8"
    }
    # create virtual environment
    conda create -n "poandy"
    # activate virtual environment (need activate everytime before you work on repo)
    conda activate poandy
    # install requirements
    conda install --file requirements.txt
    # when done
    conda deactivate

## Linter

Use flake8 without line length limit.
If using vscode, include the following in settings.json

    "python.linting.flake8Args": ["--max-line-length=200"]

## Test

    pytest
