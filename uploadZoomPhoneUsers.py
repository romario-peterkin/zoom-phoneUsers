from get_zoom_phone_users import get_all_phone_users
from uploadToCloudStorage import upload_blob
from overwriteTable import overwriteBigQueryTable
import http.client
import json
import time
import datetime as dt
import ssl

def uploadZoomPhoneUsers(token):

    bucket_name = "zoom-data"
    source_file_name = "/tmp/zoom_phone_users.jsonl"
    destination_blob_name = "zoom_phone_users.jsonl"
    dataset = 'zoom'
    table = 'phone_users'
    uri = "gs://zoom-data/zoom_phone_users.jsonl"


    ssl._create_default_https_context = ssl._create_unverified_context
    today = dt.datetime.strftime(dt.datetime.utcnow(),'%Y-%m-%d')
    conn = http.client.HTTPSConnection("api.zoom.us")


    # Outputs list_of_all_users.txt and list_of_all_users.json
    get_all_phone_users(token)

    # Upload to Cloud storage
    upload_blob(bucket_name, source_file_name, destination_blob_name)

    # Upload bucket to BigQuery
    overwriteBigQueryTable(dataset,table,uri)

