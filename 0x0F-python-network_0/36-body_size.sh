#!/bin/bash
# Takes in a URL, sends a request, and displays the size of the response
curl -sw '\n%{size_download}\n' "$1" | grep [0-9]
