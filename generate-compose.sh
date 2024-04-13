sed -e "s/\${DB_NAME}/${DB_NAME}/g" \
    -e "s/\${DB_USER}/${DB_USER}/g" \
    -e "s/\${DB_PASSWORD}/${DB_PASSWORD}/g" \
    docker-compose.yml.template > docker-compose.yml