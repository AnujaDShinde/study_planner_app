import streamlit as st
from database import add_task, get_tasks_for_user
from datetime import date
from utils import parse_date, format_status, display_task_card

def task_deadline_page():
    st.title("📅 Task Deadlines")

    if "username" not in st.session_state:
        st.error("Please log in to access your dashboard.")
        return

    username = st.session_state["username"]

    # Task Form
    with st.form("task_form"):
        task_name = st.text_input("Task Name")
        deadline = st.date_input("Deadline", min_value=date.today())
        submitted = st.form_submit_button("Add Task")

        if submitted and task_name:
            # Save task with formatted date
            add_task(username, task_name, deadline.strftime('%Y-%m-%d'))
            st.success(f"✅ Task '{task_name}' added successfully.")

    st.subheader("Your Tasks")
    
    # Fetch tasks from the database
    tasks = get_tasks_for_user(username)
    
    if tasks:
        for task in tasks:
            task_name, deadline = task[0], task[1]  # Assuming task is a tuple (task_name, deadline)
            # Format and display each task (you can customize this further)
            st.write(f"📌 **{task_name}** — Due: `{parse_date(deadline)}` {format_status(deadline)}")
    else:
        st.info("You have no tasks yet. Start by adding one above.")
