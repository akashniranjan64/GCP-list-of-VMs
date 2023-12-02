#!/bin/bash
#echo "PROJECT NAME, INSTANCE NAME , ZONE , MACHINE-TYPE , OPERATING SYSTEM , CPU , MEMORY , DISK SIZE" > compute-engine-details.csv
while read i; do
           echo "Setting Project: $i"
           echo $(gcloud config set project $i)
           if [[ $(gcloud services list --enabled --filter="NAME:composer.googleapis.com" --format="value(NAME)" | grep composer) ]]; then
               echo "composer API is enabled is in project - $i"
               echo $i >> composer-env-details.csv
               echo $(gcloud composer environments list --locations=northamerica-northeast1 | tr -cd '[:alpha:][:space:][:digit:]-' | awk '{print $1}' | tail -n +4 >> composer-env-details.csv)
           else
               echo "Compute API is not enabled in project - $i"
           fi
done < list.txt
