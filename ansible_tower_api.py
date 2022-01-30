from sys import exit
import requests

# endpoints
from endpoints import JOB_TEMPLATE_URI
from utils.handle_load_config import __load_config

# exception types
FILE_NOT_FOUND_EXCEPTION = 1
UNKNOWN_EXCEPTION = 2

# configuration file path
CONFIG_FILE_PATH = "./config/config.json"


# load the configuration
try:
    (authorization_header, CREDENTIALS, CONFIG,
     TOWER_BASE_URL) = __load_config(CONFIG_FILE_PATH)
    VERIFY_SSL = CONFIG["VERIFY_SSL"]
except Exception as e:
    print("SOME ERROR OCCURRED :: ", e)
    exit(UNKNOWN_EXCEPTION)


# get the job template details
def __get_job_template_details(job_id, base_url):

    try:
        job_template_response = requests.get(base_url+JOB_TEMPLATE_URI.format(job_id), headers={

            "Content-Type": "application/json",
            "Authorization": authorization_header

        }, verify=VERIFY_SSL)
        return job_template_response.json()
    except Exception as e:
        print("SOME ERROR OCCURRED :: ", e)
        exit(UNKNOWN_EXCEPTION)

# launch the job template


def launch_job_template(job_id, base_url):

    try: 
        job_details =  __get_job_template_details(job_id,base_url)

        requests.post(base_url+JOB_TEMPLATE_URI.format(job_id), headers={
            
            "Content-Type": "application/json",
            "Authorization": authorization_header

        }, verify=VERIFY_SSL)
    except Exception as e:
        print("SOME ERROR OCCURRED :: ", e)
        exit(UNKNOWN_EXCEPTION)

launch_job_template(7, TOWER_BASE_URL)
