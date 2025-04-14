import streamlit as st
from database import add_task, get_tasks_for_user, update_task_status
from utils import get_status_color
from datetime import date

def task_deadline_page():
    st.title("📅 Your Study Dashboard")

    if "username" not in st.session_state:
        st.warning("Please log in to continue.")
        return

    username = st.session_state["username"]

    st.subheader("➕ Add a New Task")
    task = st.text_input("Task")
    deadline = st.date_input("Deadline", min_value=date.today())
    status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])

    if st.button("Add Task"):
        if task:
            add_task(username, task, str(deadline), status)
            st.success("Task added successfully!")
        else:
            st.error("Please enter a task name.")

    st.subheader("📋 Your Tasks")
    tasks = get_tasks_for_user(username)
    if not tasks:
        st.info("No tasks yet. Start by adding one!")
    else:
        for t in tasks:
            task_id, task, deadline, status = t
            st.markdown(
                f"""
                <div style='border: 1px solid #ccc; padding: 10px; margin-bottom: 10px;
                            border-radius: 10px; background-color: {get_status_color(status)}'>
                    <b>Task:</b> {task}<br>
                    <b>Deadline:</b> {deadline}<br>
                    <b>Status:</b> 
                    <form method='post'>
                        <select name='status_{task_id}' onchange='this.form.submit()'>
                            <option {"selected" if status == "Pending" else ""}>Pending</option>
                            <option {"selected" if status == "In Progress" else ""}>In Progress</option>
                            <option {"selected" if status == "Completed" else ""}>Completed</option>
                        </select>
                    </form>
                </div>
                """,
                unsafe_allow_html=True
            )
            new_status = st.selectbox("Update Status", ["Pending", "In Progress", "Completed"], index=["Pending", "In Progress", "Completed"].index(status), key=f"status_{task_id}")
            if st.button(f"Update Status for Task {task_id}"):
                update_task_status(task_id, new_status)
                st.success("Status updated!")
                st.experimental_rerun()
