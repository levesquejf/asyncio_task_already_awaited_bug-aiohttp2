#!/usr/bin/env bash

set -euxo pipefail

docker build -t asyncio-bug-aiohttp2-native -f Dockerfile-native .
docker run asyncio-bug-aiohttp2-native
