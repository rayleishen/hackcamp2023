# grab stuff from database

from time import sleep
import json

import sys

sys.path.insert(1, '/apps')

#dbgrab#
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('json/firebase_config.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://social-seafarer-default-rtdb.firebaseio.com"
})

def maincode():
    url_ref = db.reference("/requests/" + str(x) + "/url/")
    email_ref = db.reference("/requests/" + str(x) + "/email/")
    #key_ref = db.reference("/requests/" + str(x) + "/key/")
    ntc_ref = db.reference("/requests/" + str(x) + "/num_top_comments/")
    sv_ref = db.reference("/requests/" + str(x) + "/sens_vadar/")
    sr_ref = db.reference("/requests/" + str(x) + "/sens_rake/")


    url = url_ref.get()
    email = email_ref.get()


    request_data = {
        "url": url,
        "email": email,
        "num_top_comments": num_top_comments,
        "sens_vadar": sens_vadar,
        "sens_rake": sens_rake,
    }

    with open('json/request.json', 'w') as f:
        json.dump(request_data, f)

    #main#
    import modules._database as redditscrapper
    
    
    
url_ref = db.reference("/requests/" + str(x) + "/url/")
new = url_ref.get()
old = new

while True:
    url_ref = db.reference("/requests/" + str(x) + "/url/")
    new = url_ref.get()
    sleep(2.0)
    
    print(".")
    
    if new == old:
        continue
    else:
        print("new request")
        old = new
        maincode()