#!/bin/bash

BASE_DIR=$(dirname "$0")
PROJECT_ROOT=$(cd "$BASE_DIR/.."; pwd -P)
PKG_DIR="$PROJECT_ROOT/gogolook"
TEST_DIR="$PROJECT_ROOT/tests"

autoflake \
    --recursive \
    --in-place \
    --exclude=__init__.py \
    --remove-all-unused-imports \
    --remove-unused-variables \
    --check \
    $PKG_DIR $TEST_DIR
black --check $PKG_DIR $TEST_DIR
isort --check $PKG_DIR $TEST_DIR
