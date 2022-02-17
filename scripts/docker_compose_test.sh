#!/bin/bash

set -e

BASE_DIR=$(dirname "$0")
PROJECT_ROOT=$(cd "$BASE_DIR/.."; pwd -P)

docker-compose \
    --project-directory $PROJECT_ROOT \
    -f $PROJECT_ROOT/deployment/docker-compose/docker-compose.yml \
    -f $PROJECT_ROOT/deployment/docker-compose/docker-compose.dev.yml \
    up -d

docker-compose \
    --project-directory $PROJECT_ROOT \
    -f $PROJECT_ROOT/deployment/docker-compose/docker-compose.yml \
    -f $PROJECT_ROOT/deployment/docker-compose/docker-compose.dev.yml \
    exec -T apiserver pip install .[test]

docker-compose \
    --project-directory $PROJECT_ROOT \
    -f $PROJECT_ROOT/deployment/docker-compose/docker-compose.yml \
    -f $PROJECT_ROOT/deployment/docker-compose/docker-compose.dev.yml \
    exec -T apiserver pytest
