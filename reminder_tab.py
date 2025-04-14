import streamlit as st
from email_utils import send_reminder_email
from database import get_tasks_for_user
from database import get_tasks_by_username

def reminder_tab():
    st.title("📬 Email Reminders")
    if "username" in st.session_state:
        if st.button("Send Reminder Email"):
            tasks = get_tasks_for_user(st.session_state["username"])
            if tasks:
                send_reminder_email(st.session_state["username"], tasks)
                st.success("Reminder email sent!")
            else:
                st.warning("No tasks to send reminders for.")
    else:
        st.warning("Please log in to use email reminders.")