#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response. No pipes, redirections, etc.
curl -s -o /dev/null -w "%{http_code}" "$1"
