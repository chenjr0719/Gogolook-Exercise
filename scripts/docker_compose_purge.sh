#!/bin/bash

BASE_DIR=$(dirname "$0")
PROJECT_ROOT=$(cd "$BASE_DIR/.."; pwd -P)

docker-compose \
    --project-directory $PROJECT_ROOT \
    -f $PROJECT_ROOT/deployment/docker-compose/docker-compose.yml \
    down --remove-orphans --volumes
