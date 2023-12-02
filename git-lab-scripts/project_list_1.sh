#!/bin/bash

# Set the GitLab API endpoint and access token
GITLAB_API_ENDPOINT="https://gitlab.xxxx.ca/api/v4"
GITLAB_ACCESS_TOKEN="xxxxxxx"

# Set the GitLab project ID and folder path
PROJECT_ID="1309"
FOLDER_PATH="aps"

# Call the GitLab API to get the list of subfolders
curl --header "PRIVATE-TOKEN: $GITLAB_ACCESS_TOKEN" \
  "$GITLAB_API_ENDPOINT/projects/$PROJECT_ID/repository/tree?recursive=true&path=$FOLDER_PATH" \
  | jq '.[].path' \
  | sed 's/"//g'
