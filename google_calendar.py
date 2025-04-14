import os
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from database import get_tasks_for_user
import streamlit as st

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Place your service account file in the project root

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def sync_tasks_to_calendar(username):
    service = build('calendar', 'v3', credentials=credentials)
    tasks = get_tasks_for_user(username)

    for task in tasks:
        title, description, due_date_str, status = task[2], task[3], task[4], task[5]
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        event = {
            'summary': title,
            'description': description,
            'start': {'dateTime': due_date.isoformat() + 'T09:00:00', 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': (due_date + timedelta(hours=1)).isoformat() + 'T10:00:00', 'timeZone': 'Asia/Kolkata'},
        }
        service.events().insert(calendarId='primary', body=event).execute()


def calendar_sync_tab():
    st.title("📅 Sync with Google Calendar")
    if "username" in st.session_state:
        if st.button("Sync Tasks to Google Calendar"):
            sync_tasks_to_calendar(st.session_state["username"])
            st.success("Tasks synced to Google Calendar successfully!")
    else:
        st.warning("Please log in to sync tasks.")