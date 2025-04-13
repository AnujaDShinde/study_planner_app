import streamlit as st
from database import get_tasks_by_user

def reminder_tab():
    # Check if the user is logged in
    if "username" not in st.session_state:
        st.warning("Please log in to access reminders.")
        return

    # Fetch tasks for the logged-in user
    username = st.session_state["username"]
    tasks = get_tasks_by_user(username)

    # Display tasks
    if tasks:
        st.subheader(f"Your Tasks for {username}")
        for task in tasks:
            task_name, due_date, status = task[2], task[3], task[4]
            st.write(f"Task: {task_name} - Due: {due_date} - Status: {status}")
    else:
        st.info("You don't have any tasks yet.")
