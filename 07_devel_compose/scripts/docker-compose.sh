#!/bin/sh

exec docker-compose -f docker-compose.yml -f docker-compose.devel.yml "$@"