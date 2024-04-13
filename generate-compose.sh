#!/bin/bash

# Replace placeholder variables in docker-compose.yml
sed -i "s/\${DB_NAME}/${DB_NAME}/g" docker-compose.yml
sed -i "s/\${DB_USER}/${DB_USER}/g" docker-compose.yml