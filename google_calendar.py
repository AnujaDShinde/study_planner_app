# Google Calendar integration logic
import streamlit as st
from database import get_tasks_by_user

def export_to_google_calendar():
    username = st.session_state.get("username", None)
    if not username:
        st.warning("Please log in to export tasks to Google Calendar.")
        return

    tasks = get_tasks_by_user(username)
    if not tasks:
        st.warning("No tasks found to export.")
        return

    for task in tasks:
        task_name, due_date, _ = task[2], task[3], task[4]
        # You can replace the line below with actual Google Calendar API integration
        st.write(f"Pretending to export: {task_name} due on {due_date}")

    st.success("Tasks exported to Google Calendar (demo mode).")
