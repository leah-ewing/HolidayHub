#!/bin/bash

# Replace placeholder variables
sed -i "s/\${DB_NAME}/${DB_NAME}/g" docker-compose.yml