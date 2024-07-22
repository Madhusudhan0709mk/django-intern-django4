import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from django.conf import settings

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = os.path.join(settings.BASE_DIR, settings.GOOGLE_CALENDAR_CREDENTIALS)

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('calendar', 'v3', credentials=credentials)

def create_google_calendar_event(appointment):
    event = {
        'summary': f'Appointment with {appointment.patient.name}',
        'start': {
            'dateTime': f'{appointment.date}T{appointment.start_time}',
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': f'{appointment.date}T{appointment.end_time}',
            'timeZone': 'UTC',
        },
    }
    calendar_id = 'primary'
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
