import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email reminder
def send_email_reminder(to_email, subject, message):
    from_email = "your_email@example.com"  # Replace with your email
    password = "your_email_password"       # Replace with your email password

    try:
        # Set up the server and send the email
        smtp_server = "smtp.gmail.com"
        port = 465  # For SSL
        context = ssl.create_default_context()

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, "plain"))

        # Connect to the server and send the email
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
