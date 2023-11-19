# grab stuff from databas s

import smtplib, json
from time import sleep

with open('json/config.json') as config_file:
    data = json.load(config_file)


#firebase db stuff
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('json/firebase_config.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://social-seafarer-default-rtdb.firebaseio.com"
})

x=1
email_ref = db.reference("/requests/" + str(x) + "/email/")
name_ref = db.reference("/requests/" + str(x) + "/name/")
body_ref = db.reference("/requests/" + str(x) + "/body/")

email = str(email_ref.get())
name = str(name_ref.get())
body = str(body_ref.get())

