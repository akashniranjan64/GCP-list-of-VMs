#!/bin/bash
gcloud config set account infra-admin-sa@playground-aps-sre-sb.iam.gserviceaccount.com
gsutil cp start_feed.csv stop_feed.csv  gs://scheduler-source
