#!/bin/bash
type=$1
while read i; do
           echo "Setting Project: $i"
           echo $(gcloud config set project $i)
           if [[ $(gcloud services list --enabled --filter="NAME:compute.googleapis.com" --format="value(NAME)" | grep compute) ]]; then
               echo "Compute API is enabled is in project - $i"
               echo $(gcloud compute instances list | awk '{print $1,$2,$5}' | tail -n +2 | while read line; do echo "$i $line"; done |xargs -n4 sh -c 'python3  '$type'-vm.py $1 $2 $3 $4 >> vm-label-keepalive.csv' sh ) #
           else
               echo "Compute API is not enabled in project - $i"
           fi
done < project-list.txt