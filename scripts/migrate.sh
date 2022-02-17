#!/bin/bash

BASE_DIR=$(dirname "$0")
PROJECT_ROOT=$(cd "$BASE_DIR/.."; pwd -P)
MIGRATIONS_DIR="$PROJECT_ROOT/gogolook/db/migrations"
CUR_DIR=$PWD

cd $MIGRATIONS_DIR
alembic upgrade head
cd $CUR_DIR
