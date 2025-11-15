#!/bin/bash

# Name deines Containers
CONTAINER_NAME="control-app"

echo "🛑 Stoppe Container: $CONTAINER_NAME ..."
docker stop "$CONTAINER_NAME"

echo "🧹 Entferne Container: $CONTAINER_NAME ..."
docker rm "$CONTAINER_NAME"

echo "✅ Container gestoppt und entfernt."