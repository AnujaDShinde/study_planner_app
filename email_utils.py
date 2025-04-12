# Weekly reminder emails using yagmail
import smtplib
from email.message import EmailMessage
import streamlit as st
from database import get_tasks_by_user

EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_app_password"

def send_email_reminder():
    username = st.session_state.get("username", None)
    user_email = st.session_state.get("email", None)

    if not username or not user_email:
        st.warning("Please log in to send reminders.")
        return

    tasks = get_tasks_by_user(username)
    if not tasks:
        st.warning("No tasks to include in the email.")
        return

    message = EmailMessage()
    message["Subject"] = "Study Planner Task Reminder"
    message["From"] = EMAIL_SENDER
    message["To"] = user_email

    body = f"Hi {username},\n\nHere are your tasks:\n\n"
    for task in tasks:
        task_name, due_date, status = task[2], task[3], task[4]
        body += f"- {task_name} (Due: {due_date}, Status: {status})\n"

    body += "\nBest of luck with your studies!\n\nStudy Planner App"
    message.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(message)
        st.success("Email reminder sent successfully!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")
