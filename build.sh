#!/bin/bash
PWD=$(pwd)
ucc-gen
cd output/
tar -cvzf TA-jira-service-desk-simple-addon.tgz TA-jira-service-desk-simple-addon
cd "$PWD"
exit 0
