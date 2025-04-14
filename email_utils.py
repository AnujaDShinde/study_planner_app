import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from database import get_tasks_by_username, get_user_email
from datetime import datetime, timedelta

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_ADDRESS = "shindeanujadr01@gmail.com"
EMAIL_PASSWORD = "Anuja@Shinde01"


def send_email(recipient, subject, body):
    try:
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))

        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)
        server.quit()

    except Exception as e:
        print(f"❌ Failed to send email: {e}")


def send_reminder_email(username):
    user_email = get_user_email(username)
    tasks = get_tasks_by_username(username)
    today = datetime.today().date()
    upcoming = [t for t in tasks if datetime.strptime(t[3], "%Y-%m-%d").date() == today]

    if upcoming:
        task_list = "".join([f"<li>{t[2]} - Due: {t[3]} (Status: {t[4]})</li>" for t in upcoming])
        body = f"""
        <h3>📌 Today's Task Reminder</h3>
        <ul>{task_list}</ul>
        <p>Stay focused and good luck! 💪</p>
        """
        send_email(user_email, "📚 Study Planner - Today's Tasks", body)


def send_weekly_summary(username):
    user_email = get_user_email(username)
    tasks = get_tasks_by_username(username)
    one_week = datetime.today() + timedelta(days=7)
    upcoming = [t for t in tasks if datetime.strptime(t[3], "%Y-%m-%d").date() <= one_week.date()]

    if upcoming:
        task_list = "".join([f"<li>{t[2]} - Due: {t[3]} (Status: {t[4]})</li>" for t in upcoming])
        body = f"""
        <h3>📅 Weekly Study Summary</h3>
        <p>Here are your upcoming tasks for the week:</p>
        <ul>{task_list}</ul>
        <p>Stay consistent and keep learning! 🚀</p>
        """
        send_email(user_email, "📈 Study Planner - Weekly Summary", body)