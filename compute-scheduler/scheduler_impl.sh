#!/bin/bash
computelist=$1
projectname=$2
task=$3

if gcloud projects describe $projectname &>/dev/null; then
            echo "Setting Project: $projectname"
            echo $(gcloud config set project $projectname)
             if [[ $(gcloud services list --enabled --filter="NAME:compute.googleapis.com" --format="value(NAME)" | grep compute) ]]; then
                 echo "Compute API is enabled is in project - $projectname"
                 echo $(gcloud compute instances list | grep -E $computelist | awk '{print $1,$2}' | tail -n +1 | while read line; do echo "$projectname $line"; done |xargs -n3 sh -c 'python3  '$task'-vm.py $1 $2 $3' sh)
             else
                 echo "Compute API is not enabled in project - $projectname"
             fi
else
  echo "Project does not exist"
fi