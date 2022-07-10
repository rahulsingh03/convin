from django import http
from django.shortcuts import redirect, render,HttpResponse
from googleapiclient.discovery import build
from datetime import timedelta
import datetime
import pytz
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account


def GoogleCalendarInitView(request):
    CLIENT_SECRET_FILE = 'oauth_secret_key.json'

    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, scopes=scopes)

    flow.run_local_server()
    credentials = flow.credentials
    global service
    service = build('calendar', 'v3', credentials=credentials)
    return redirect('/rest/v1/calendar/redirect/')
    

def GoogleCalendarRedirectView(request):
    try:
        getcalId = service.calendarList().list().execute()
        calId = getcalId['items'][0]['id']
        res = service.events().list(calendarId=calId).execute()
        
    except NameError:
        return HttpResponse('Please reload with path ~~ rest/v1/calendar/init/ ')
        
    return HttpResponse(res.items())
        







# service_account_email = 'ur email ID'
# def build_service(request):
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(
#         filename=CLIENT_SECRET_FILE,
#         scopes=scopes
#         )

        
    # http = credentials.authorize(httplib2.Http())


    #     service = build('calendar', 'v3', http=http)

#     return service

# def create_event(request):
#     service = build_service(request)

#     start_datetime = datetime.datetime.now(tz=pytz.utc)
#     event = service.events().insert(calendarId='rsb55426@gmail.com', body={
#         'summary': 'Foo',
#         'description': 'Bar',
#         'start': {'dateTime': start_datetime.isoformat()},
#         'end': {'dateTime': (start_datetime + timedelta(minutes=15)).isoformat()},
#     }).execute()

#     return HttpResponse(event.items())