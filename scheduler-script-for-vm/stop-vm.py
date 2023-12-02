from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

import re
import sys

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)

if (len(sys.argv)) >=3:
    project = sys.argv[1]
    instance = sys.argv[2]
    zone = sys.argv[3]

    # Stop instances
    #compute.instances().stop(project=SOURCE_PROJECT, zone='us-central1-a', instance=VM_NAME).execute()

    request = service.instances().stop(project=project, zone=zone, instance=instance)
    response = request.execute()

    print(f'{project},{instance},{zone}')
    print(" Stopped ")