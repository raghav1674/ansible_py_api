import requests

# oauth endpoints 
from endpoints import AUTH_CODE_ENDPOINT,TOKEN_ENDPOINT


# get the auth code
def __get_auth_code(base_url, client_id, redirect_uri,response_type='code'):
    auth_url = f'{base_url}{AUTH_CODE_ENDPOINT}?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}'
    print("Visit ",auth_url)

# get the access token
def __get_access_token(base_url, client_id, client_secret, redirect_uri, code, verify_ssl,grant_type="authorization_code"):

    token_response = requests.post(base_url+TOKEN_ENDPOINT, data={

        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "code": code,
        "grant_type": grant_type
    },
     verify=verify_ssl)

    response = token_response.json()
    
    return {

        "access_token" : response["access_token"],
        "token_type" : response["token_type"],
        "refresh_token" : response["refresh_token"]
    }
   

def __get_creds(base_url,client_id,client_secret,redirect_uri,verify_ssl):
    __get_auth_code(base_url,
              client_id, redirect_uri)
    auth_code = input("Enter Auth Code: ")
    return __get_access_token(base_url,
                client_id, client_secret, redirect_uri, auth_code,verify_ssl)



