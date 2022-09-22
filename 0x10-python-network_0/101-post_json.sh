#!/bin/bash
#Sends a JSON POST request to a url passed as the first argument and displays the body of the response
curl -sX POST --data @"$2" --header "Content-Type: application/json" "$1"
