#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server
curl -I -X OPTIONS -s "$1" | grep 'Allow:' | tr -d '\r\n' | sed 's/Allow: //'
