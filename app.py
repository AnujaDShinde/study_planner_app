import streamlit as st
from reminder_tab import reminder_tab  # Ensure this import is correct
from signup import signup_page  # Ensure this import is correct
from task_deadlines import task_deadline_page
from database import create_tables

# Initialize database
create_tables()

def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "Login"

    # Sidebar
    with st.sidebar:
        st.title("📚 Study Planner")
        if "username" in st.session_state:
            st.write(f"👤 Logged in as: {st.session_state['username']}")
            if st.button("Dashboard"):
                st.session_state["page"] = "Dashboard"
            if st.button("Email Reminders"):
                st.session_state["page"] = "Reminder"
            if st.button("Log Out"):
                st.session_state.clear()
                st.success("You have been logged out.")
        else:
            if st.button("Login"):
                st.session_state["page"] = "Login"
            if st.button("Sign Up"):
                st.session_state["page"] = "Signup"

    # Page content
    page = st.session_state["page"]

    if page == "Login":
        signup_page()  # Calling the signup_page function here
    elif page == "Signup":
        signup_page()  # Calling the signup_page function here
    elif page == "Dashboard":
        task_deadline_page()
    elif page == "Reminder":
        reminder_tab()

if __name__ == "__main__":
    main()
