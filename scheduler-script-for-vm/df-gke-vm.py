from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import json
import re
import sys

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)
instance_pattern = '^(dataflow|gke|df-|bespoke|dpdi)'
counter = False

def instance_name():
    if counter == False:
        print(instance)

def df_vms(vm_meta_js):
    global counter
    for key in vm_meta_js:
        if 'metadata' in key:
            meta_js = json.dumps(vm_meta_js['metadata'])
            meta_js_load = json.loads(meta_js)
            if 'items' in meta_js_load:
                item = meta_js_load['items'] # this is the list of items values in dictionary format
                for dictionary in item:
                    if 'dataproc-cluster-name' in dictionary['key']: #goog-dataproc-cluster-uuid
                        counter = True
                instance_name()

if (len(sys.argv)) >= 3:
    if not re.match(instance_pattern, sys.argv[2]):
        project = sys.argv[1]
        instance = sys.argv[2]
        zone = sys.argv[3]
        status = sys.argv[4]

        request = service.instances().get(project=project, zone=zone, instance=instance)
        response = request.execute()

        vm_meta_response = json.dumps(response)
        vm_meta_response_data = json.loads(vm_meta_response)

        df_vms(vm_meta_response_data)