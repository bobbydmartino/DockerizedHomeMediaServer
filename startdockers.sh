#!/bin/bash

docker-compose -f docker-compose.yml -d
./plex_build/generate_container.sh --run
