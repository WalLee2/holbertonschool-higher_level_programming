#!/bin/bash
# Script that takes a URL, sends a POST request to the URL, and display response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
