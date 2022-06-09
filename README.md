# Friendly Reminder

[![issues](https://img.shields.io/github/issues/rluetzner/friendly-reminder)](https://github.com/rluetzner/friendly-reminder/issues)
[![forks](https://img.shields.io/github/forks/rluetzner/friendly-reminder)](https://github.com/rluetzner/friendly-reminder/network/members)
[![stars](https://img.shields.io/github/stars/rluetzner/friendly-reminder)](https://github.com/rluetzner/friendly-reminder/stargazers)
[![license](https://img.shields.io/github/license/rluetzner/friendly-reminder)](COPYING)

This CLI app wants to help you stay in touch with your friends.

## Installation

```bash
# TODO
```

## Usage

Here's a quick overview on how this tool is meant to be used.

```text
# Add a reminder for Mom and Omar Cabbage.
$ friendly-reminder add --name "Mom"
Added Mom succesfully.
$ friendly-reminder add --name "Omar Cabbage"
Added Omar Cabbage succesfully.

# Check if there are any reminders for today.
$ friendly-reminder check
Nothing for today.
# See the list of upcoming check-ins.
$ friendly-reminder check --all
Think about contacting:
Mom (7 days)
Omar Cabbage (7 days)

# Set the date where we last contacted Omar Cabbage.
$ friendly-reminder update --name "Omar Cabbage" --last-contact 2022-03-27
Updated Omar Cabbage succesfully.

# Recheck our reminders for today.
$ friendly-reminder check
Think about contacting:
Omar Cabbage (-9 days)

# I've talked to Omar today.
$ friendly-reminder renew --name "Omar Cabbage"
Updated Omar Cabbage succesfully.

# 'Unfriend' mom. Don't try this at home. ;-)
$ friendly-reminder remove --name Mom
Removed Mom succesfully.

# Use --help if you are stuck.
```

You can easily automate `check` with a cronjob, i.e. if you've got Termux
installed on your Android phone:

```bash
crontab -e
# The following line will send you a notification every morning at 9.
# 0 9 * * * friendly-reminder check | termux-notification --title Friendly-Reminder
```

## Developer setup

```bash
# Do we have to tell people to install Go???
```

## Install from source

```bash
# go install
```
