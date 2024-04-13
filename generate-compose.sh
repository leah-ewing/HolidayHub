#!/bin/bash

# Replace placeholder variables from Secrets
sed -i "s/\${DB_NAME}/${DB_NAME}/g" docker-compose.yml