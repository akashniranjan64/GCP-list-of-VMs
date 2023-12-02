#!/bin/bash


echo "PROJECT NAME, INSTANCE NAME , ZONE , MACHINE-TYPE , OPERATING SYSTEM , CPU , MEMORY , DISK SIZE" > compute-engine-details.csv
#prjs=( $(gcloud projects list | tail -n +2 | awk {'print $1'}) )

for i in "${prjs[@]}"
    do
        echo "Setting Project: $i"
        echo $(gcloud config set project $i)
        if [[ $(gcloud services list --enabled --filter="NAME:compute.googleapis.com" --format="value(NAME)" | grep compute) ]]; then
            echo "Compute API is enabled is in project - $i"
            echo $(gcloud compute instances list | awk '{print $1,$2}' | tail -n +2| while read line; do echo "$i $line"; done |xargs -n3 sh -c 'python3  retrieve-compute-engine-details.py $1 $2 $3 >> compute-engine-details.csv' sh)
        else
            echo "Compute API is not enabled in project - $i"
        fi
    done