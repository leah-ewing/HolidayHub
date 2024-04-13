sed -e "s/\${DB_NAME}/${DB_NAME}/g" \
    -e "s/\${DB_USER}/${DB_USER}/g" \
    docker-compose.yml.template > docker-compose.yml