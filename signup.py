import streamlit as st
from database import add_user, get_user, authenticate_user

def signup_page():
    st.title("Sign Up")

    # User input
    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")
    email = st.text_input("Email")

    # Check if username already exists
    if st.button("Sign Up"):
        if get_user(username):
            st.error("Username already exists!")
        else:
            add_user(username, password, email)
            st.success("User registered successfully!")

            # Set session state and redirect
            st.session_state["username"] = username
            st.session_state["page"] = "Dashboard"
            st.write("Redirecting to dashboard...")

def login_page():
    st.title("Login")

    # User input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state["username"] = username
            st.success("Login successful!")
            st.session_state["page"] = "Dashboard"
            st.write("Redirecting to dashboard...")
        else:
            st.error("Invalid username or password")
