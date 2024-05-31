#!/bin/bash

# Copy new files to the application directory
cp -r /tmp/deployment-archive/* /HolidayHub

# Set file permissions
chown -R ubuntu:ubuntu /HolidayHub

# Activate the virtual environment
source env/bin/activate

# Install dependancies
pip3 install -r requirements.txt

# Source secrets
source .env.production

# Set secrets permissions
sudo chmod 600 /HolidayHub/.env.production

# Seed database
python3 database/seed_database.py

# Restart the service
sudo systemctl daemon-reload
sudo systemctl start holidayhub.service