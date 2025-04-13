import streamlit as st
from datetime import date
from database import add_task, get_tasks_for_user, update_task_status

def task_deadline_page():
    st.title("📅 Task Deadlines")

    if "username" not in st.session_state:
        st.error("Please log in to access this section.")
        return

    username = st.session_state["username"]

    # --- Add Task Form ---
    with st.form("add_task_form"):
        task_name = st.text_input("Enter Task Name")
        deadline = st.date_input("Select Deadline", min_value=date.today())
        submitted = st.form_submit_button("Add Task")

        if submitted and task_name:
            add_task(username, task_name, str(deadline))
            st.success(f"✅ Task '{task_name}' added!")

    # --- View Tasks ---
    st.subheader("🗂️ Your Tasks")
    tasks = get_tasks_for_user(username)

    if not tasks:
        st.info("No tasks found. Add your first task above.")
        return

    status_options = ["Pending", "In Progress", "Completed"]

    for task in tasks:
        task_id, task_name, due_date, status = task
        col1, col2, col3 = st.columns([3, 2, 2])
        with col1:
            st.markdown(f"**📌 {task_name}**  \n📅 Due: `{due_date}`")
        with col2:
            new_status = st.selectbox("Status", status_options, index=status_options.index(status), key=task_id)
        with col3:
            if new_status != status:
                update_task_status(task_id, new_status)
                st.success(f"✅ Status updated to '{new_status}'")
