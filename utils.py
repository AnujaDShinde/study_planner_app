# Helper functions for personalization
import datetime
import streamlit as st

# Convert a date string (YYYY-MM-DD) to a datetime.date object
def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

# Format task status for consistent display
def format_status(status):
    status_map = {
        "pending": "🟡 Pending",
        "completed": "✅ Completed",
        "overdue": "🔴 Overdue"
    }
    return status_map.get(status.lower(), status)

# Validate email format
def is_valid_email(email):
    return "@" in email and "." in email

# Validate password strength
def is_strong_password(password):
    return len(password) >= 6

# Show task as styled card (optional UI helper)
def display_task_card(task):
    task_name, due_date, status = task[2], task[3], task[4]
    st.markdown(f"""
    <div style="background-color:#262730; padding:10px; border-radius:10px; margin-bottom:10px;">
        <strong>{task_name}</strong><br>
        📅 Due: {due_date}<br>
        🏷️ Status: {format_status(status)}
    </div>
    """, unsafe_allow_html=True)
