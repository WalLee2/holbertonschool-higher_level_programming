#!/bin/bash
# Send a JSON POST request to a URL and display the body of the response
curl -sH "Content-Type: application/json" -d @"$2" "$1"
