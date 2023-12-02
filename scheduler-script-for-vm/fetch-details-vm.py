from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import json
import re
import sys

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)
instance_pattern = '^(dataflow|gke|df-|bespoke|dpdi|gc-ce|perform|dpc|dpap|gcs-|nb-|dplt|runner-|local-|lmedia-|hub-|notebook-|sdm-|gcp-|dp-|ptp-|apa-)'



if (len(sys.argv)) >= 3:
    if not re.match(instance_pattern, sys.argv[2]):
        project = sys.argv[1]
        instance = sys.argv[2]
        zone = sys.argv[3]
        status = sys.argv[4]

        request = service.instances().get(project=project, zone=zone, instance=instance)
        response = request.execute()
        json_response = json.dumps(response)
        data = json.loads(json_response)
        print(data)