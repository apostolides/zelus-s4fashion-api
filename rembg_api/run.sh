#!/bin/bash

docker build -t rembgapi .
docker run --rm -p 8000:8000 rembgapi