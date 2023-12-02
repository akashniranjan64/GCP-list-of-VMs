#!/bin/bash
while read i; do
           if [[ $(gcloud services list --enabled --filter="NAME:compute.googleapis.com" --format="value(NAME)" | grep compute) ]]; then
               echo $(gcloud config set project $i)

               echo $(gcloud compute instances list | awk '{print $1,$2}' | tail -n +2 | while read name zone; do \
                 js=$(gcloud compute instances describe $name --zone=$zone --format=json | jq -r '.labels')
                  if [[ $(echo $js | jq 'has("goog-dataproc-cluster-name")') == false && $(echo $js | jq 'has("dataflow_job_id")') == false ]]; then
                            echo $name , $i >> vm-label-keepalive.csv
                  fi; done)
           else
               echo "Compute API is not enabled in project - $i"
           fi
done < project-list.txt