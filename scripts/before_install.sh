#!/bin/bash


# Check if the script has executable permissions
if [ ! -x "$0" ]; then
    # If not, set executable permissions
    sudo chmod +x "$0"
fi

# Set executable permissions for after_install.sh
sudo chmod +x /scripts/after_install.sh

# Change to app root directory
cd /HolidayHub

# Stop app service
sudo systemctl stop holidayhub.service

# Remove all repo files for replacement, leave important files
find . -mindepth 1 ! -name 'encryption.py' ! -name '.env.production' ! -path './env*' ! -path './encryption*' ! -print0 | xargs -0 rm -rf
