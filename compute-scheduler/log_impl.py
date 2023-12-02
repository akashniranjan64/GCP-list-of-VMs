import logging

def _init_logger():
    logger = logging.getLogger('app')
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('/Users/akasnir/Documents/loblaw/Stories/GCP-list-of-VMs/compute-scheduler/myapp.log')
    #handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(created)f : %(asctime)s : %(pathname)s : %(lineno)s : %(levelname)s : %(name)s : %(module)s : %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger