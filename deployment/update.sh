#!/bin/bash
cd ~/softwarecite.com/deployment
git pull
docker compose -f docker-compose.prod.yml up -d --build
# FIXME: to make sure static files are updated
docker exec deployment-web-1 bash -c "python manage.py collectstatic --no-input"
