# Friendly Reminder

[![issues](https://img.shields.io/github/issues/rluetzner/friendly-reminder)](https://github.com/rluetzner/friendly-reminder/issues)
[![forks](https://img.shields.io/github/forks/rluetzner/friendly-reminder)](https://github.com/rluetzner/friendly-reminder/network/members)
[![stars](https://img.shields.io/github/stars/rluetzner/friendly-reminder)](https://github.com/rluetzner/friendly-reminder/stargazers)
[![license](https://img.shields.io/github/license/rluetzner/friendly-reminder)](COPYING)

This CLI app wants to help you stay in touch with your friends.

## Install

```bash
python setup.py install
```

## Developer setup

```bash
# (optional) Create a new virtual environment for python
python3 -m venv env
source env/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Initialise the config directory
mkdir $HOME/.config/friendly-reminder

# Run
python3 main.py
```
