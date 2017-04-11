#!/bin/bash
# Displays only the status code of the request to a URL
curl -so /dev/null -w "%{http_code}" "$1"
