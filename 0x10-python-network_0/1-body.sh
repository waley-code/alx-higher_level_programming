#!/bin/bash
# Returns body of response
response=$(curl -s "$1")
echo "$response"
