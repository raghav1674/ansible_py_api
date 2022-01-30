from json import load
import base64

from utils.handle_oauth import __get_creds

# exception types
FILE_NOT_FOUND_EXCEPTION = 1
UNKNOWN_EXCEPTION = 2


def __load_config(config_file_path):

    try:
        # read the configuration file
        with open(config_file_path, "r") as cfg:
            CONFIG = load(cfg)
            TOWER_BASE_URL = CONFIG["TOWER_BASE_URL"]  # base url of tower
            # tower access credentials
            CREDENTIALS = CONFIG["TOWER_CREDENTIALS"][CONFIG["AUTHENTICATION_TYPE"]]

        authorization_header = ''
        if CONFIG["AUTHENTICATION_TYPE"] == 'Basic':

            base64_encoded_auth = base64.b64encode(str(
                CREDENTIALS["USERNAME"]+":"+CREDENTIALS["PASSWORD"]).encode('ascii')).decode("ascii")
            authorization_header = f'Basic {base64_encoded_auth}'
        else:
            bearer_token = __get_creds(
                TOWER_BASE_URL, CREDENTIALS["USERNAME"], CREDENTIALS["PASSWORD"], CREDENTIALS["REDIRECT_URI"],CONFIG["VERIFY_SSL"])["access_token"]
            authorization_header = f'Bearer {bearer_token}'

        return (authorization_header, CREDENTIALS, CONFIG, TOWER_BASE_URL)

    except FileNotFoundError as file_exception:
        print(f"{config_file_path} Does Not Exists.")
        exit(FILE_NOT_FOUND_EXCEPTION)
    except Exception as unknown_exception:
        print("Some Exception occurred :: ", unknown_exception)
        exit(UNKNOWN_EXCEPTION)
