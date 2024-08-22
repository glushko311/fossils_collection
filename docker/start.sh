#!/bin/bash
if [ "$APP_ENV" = "production" ]; then
  ENV_FILE="../production.env"
elif [ "$APP_ENV" = "testing" ]; then
  ENV_FILE="../testing.env"
else
  ENV_FILE="../develop.env"
fi
echo "There are used $ENV_FILE config file"
docker-compose --env-file $ENV_FILE up -d