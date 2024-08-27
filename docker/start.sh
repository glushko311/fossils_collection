#!/bin/bash
if [ "$APP_ENV" = "production" ]; then
  ENV_FILE="../src/config/production.env"
elif [ "$APP_ENV" = "testing" ]; then
  ENV_FILE="../src/config/testing.env"
else
  ENV_FILE="../src/config/develop.env"
fi
echo "There are used $ENV_FILE config file"
docker-compose --env-file $ENV_FILE up -d