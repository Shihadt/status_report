"""
Shows basic usage of the Gmail API.

Lists the user's Gmail labels.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from create import create_message
from send import send_message
from my_draft import create_draft 
import sys

path = sys.argv[1] + "/"

def email_function(fro,to,cc,header,msg):
# Setup the Gmail API
    SCOPES = 'https://www.googleapis.com/auth/gmail.compose' 
    store = file.Storage(path + 'token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(path + 'credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    message = create_message(fro,to,cc,header,msg)

    create_draft(service,"me",message)
