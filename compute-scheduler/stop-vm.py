from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import re
import sys
import log_impl

logger = log_impl._init_logger()

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)

if (len(sys.argv)) >=3:
    project = sys.argv[1]
    instance = sys.argv[2]
    zone = sys.argv[3]

    request = service.instances().stop(project=project, zone=zone, instance=instance)
    response = request.execute()

    print(f'{project},{instance},{zone}')
    print(" Stopped ")