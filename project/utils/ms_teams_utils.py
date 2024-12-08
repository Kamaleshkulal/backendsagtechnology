# utils/ms_teams_utils.py
import msal
import requests
from django.conf import settings

def get_ms_token():
    app = msal.ConfidentialClientApplication(
        settings.MS_GRAPH_CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{settings.MS_GRAPH_TENANT_ID}",
        client_credential=settings.MS_GRAPH_CLIENT_SECRET
    )
    result = app.acquire_token_silent(["https://graph.microsoft.com/.default"], account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    return result['access_token']

def create_teams_meeting(subject, start_time, end_time, participants):
    access_token = get_ms_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    meeting_data = {
        "subject": subject,
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
        "attendees": [{"emailAddress": {"address": email}} for email in participants]
    }
    response = requests.post("https://graph.microsoft.com/v1.0/me/onlineMeetings", headers=headers, json=meeting_data)
    return response.json()
