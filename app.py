import streamlit as st
st.set_page_config(page_title="Study Planner App", layout="wide")  # must be first Streamlit command

from signup import main as signup_page
from task_deadlines import task_deadline_page
from database import create_tables, get_user

# Create DB tables at app launch
create_tables()

# ------------------------
# Login Function
# ------------------------
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user(username)
        if user and user[1]:  # Check if user exists
            from passlib.hash import pbkdf2_sha256
            if pbkdf2_sha256.verify(password, user[1]):
                st.session_state["username"] = username
                st.success(f"Welcome back, {username}!")
                st.session_state["page"] = "Dashboard"
            else:
                st.error("Incorrect password.")
        else:
            st.error("User not found.")

# ------------------------
# Logout Function
# ------------------------
def logout():
    st.session_state.clear()
    st.success("You have been logged out.")

# ------------------------
# Main Page Handler
# ------------------------
def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "Login"

    # Sidebar Navigation
    with st.sidebar:
        st.title("📚 Study Planner")
        if "username" in st.session_state:
            st.write(f"👤 Logged in as: {st.session_state['username']}")
            if st.button("📅 Dashboard"):
                st.session_state["page"] = "Dashboard"
            if st.button("🚪 Log Out"):
                logout()
        else:
            if st.button("🔐 Login"):
                st.session_state["page"] = "Login"
            if st.button("📝 Sign Up"):
                st.session_state["page"] = "Signup"

    # Page Rendering
    page = st.session_state["page"]

    if page == "Login":
        login()
    elif page == "Signup":
        signup_page()
    elif page == "Dashboard":
        task_deadline_page()

# ------------------------
# Run App
# ------------------------
if __name__ == "__main__":
    main()
