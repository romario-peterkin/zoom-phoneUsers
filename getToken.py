import jwt
from time import time
import http.client
import datetime
import json
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context


def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing API Key & exp time
        {"iss": os.environ.get('API_KEY'), "exp": time() + 5000},
        # Secret used to generate token signature
        os.environ.get('API_SECRET'),
        # Specify the hashing alg
        algorithm='HS256'
    )

    return token
