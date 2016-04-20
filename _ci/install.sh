#!/usr/bin/env bash

set -e
echo "Installing dependencies"
pip install -r dev-requirements.txt

echo "Downloading and unzipping odm_automation"
wget https://github.com/OpenDevelopmentMekong/odm-automation/archive/master.zip -O /tmp/odm_automation.zip
unzip /tmp/odm_automation.zip -d /tmp/
