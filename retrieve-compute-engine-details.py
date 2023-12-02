from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

import re
import sys

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)
instance_pattern = '^(dataflow|gke|df-|bespoke|dpdi|gc-ce|perform|dpc|dpap|gcs-|nb-|dplt|runner-|local-|lmedia-|hub-|notebook-|dphub-|sdm-|gcp-|dp-|ptp-|apa-)'

#print(str(sys.argv))
if (len(sys.argv)) >=3:
    if not re.match(instance_pattern, sys.argv[2]):
        project = sys.argv[1]
        instance = sys.argv[2]
        zone = sys.argv[3]
        request = service.instances().get(project=project, zone=zone, instance=instance)
        response = request.execute()

        # Get machine type
        #mtype = re.search(r'(.*)/(.*)', response['machineType']).group(2)

        # Get operating system name
        #osu = response['disks'][0]['licenses'][0]
        #os = re.search(r'(.*)/(.*)', osu).group(2)

        # Get disk size
        #dsize = str(response['disks'][0]['diskSizeGb']) + ' GB'

        # Use machine type to get cpu count & memory size
        #mrequest = service.machineTypes().get(project=project, zone=zone, machineType=mtype)
        #mresponse = mrequest.execute()

        # Get cpu count
        #cpu = mresponse['guestCpus']

        # Get memory size
        #megabyte = mresponse['memoryMb']
        #gigabyte = 1.0/1024
        #memory = str(gigabyte * megabyte) + ' GB'

        #print(f'{project},{instance},{zone},{mtype},{os},{cpu},{memory},{dsize}')
        print(f'{project},{instance},{zone}')
