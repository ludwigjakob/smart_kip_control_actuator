#!/bin/bash
set -a
source .env
set +a

# Image neu bauen
docker build -t smart_kip_control_actor .

# Container starten
docker run -d \
  --name control-app \
  --restart unless-stopped \
  --network host \
  --privileged \
  --device /dev/gpiomem \
  smart_kip_control_actor