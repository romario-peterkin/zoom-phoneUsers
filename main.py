from getToken import generateToken
from uploadZoomPhoneUsers import uploadZoomPhoneUsers
import http.client
import json
import ssl


def uploadPhoneUsers(request, payload):


    ssl._create_default_https_context = ssl._create_unverified_context


    # Get jwt token for import
    token = generateToken()

    # Upload information to Bigquery tables
    # Tables listed under the Zoom dataset in bigquery

    # users
    uploadZoomPhoneUsers(token)

    return ('Users loaded to Bigquery.')
