#!/usr/bin/env bash

set -euxo pipefail

docker build -t asyncio-bug-aiohttp2-nuitka -f Dockerfile-nuitka .
docker run asyncio-bug-aiohttp2-nuitka
