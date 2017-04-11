#!/bin/bash
# Send a DELETE request to URL and display the body of the response
curl -sL "$1" -X DELETE
