#!/bin/bash
# Change directory to your bot's location
cd /path/to/your/bot || { echo "Failed to change directory"; exit 1; }

# Activate the virtual environment
source .venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }

# Run your bot
python social_media_bot.py >> social_media_bot.log 2>&1
