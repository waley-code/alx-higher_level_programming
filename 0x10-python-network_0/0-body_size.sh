#!/bin/bash
# getting the URI from cmd
# URL=$1
# sending request and getting response
# RESPONCE=$(curl -sS $URL)
# Getting responce in bytes
# SIZE=$(echo -n $RESPONSE | wc -c)
# echo $SIZE
curl -s "$1" | wc -c
