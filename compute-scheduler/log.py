import logging.config

# Load the logging configuration from file
#logging.config.fileConfig('logging.conf')

# Get the logger
#logger = logging.getLogger('sampleLogger')

#def getloger():
#   return logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s %(levelname)s %(message)s',
#                    filename='/Users/akasnir/Documents/loblaw/Stories/GCP-list-of-VMs/compute-scheduler/myapp.log',
#                    filemode='a')

import logging

def _init_logger():
    logger = logging.getLogger('app')
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler('/Users/akasnir/Documents/loblaw/Stories/GCP-list-of-VMs/compute-scheduler/myapp.log')
    handler.setLevel(logging.INFO)
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(created)f : %(asctime)s : %(pathname)s : %(lineno)s : %(levelname)s : %(name)s : %(module)s : %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

#_init_logger()
#_logger = logging.getLogger('app')