#!/bin/bash
while read i; do
echo $i
echo "insert into VMs_list(project_name,vm_name,vm_sch_start,vm_sch_stop,vm_zone) values('$i);" >> seed.txt
done < compute-engine-details.csv