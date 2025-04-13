import streamlit as st
from database import add_user, authenticate_user

def signup_page():
    st.title("📝 Sign Up / Login")
    mode = st.radio("Choose Option", ["Sign Up", "Login"])

    if mode == "Sign Up":
        st.subheader("Create New Account")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        role = st.selectbox("Role", ["student", "teacher"])

        if st.button("Sign Up", key="signup_button"):
            if password != confirm_password:
                st.error("Passwords do not match.")
            elif not username or not email or not password:
                st.error("Please fill in all the fields.")
            else:
                try:
                    add_user(username, password, role)
                    st.success(f"Account created for {username}! You can now log in.")
                except ValueError as e:
                    st.error(str(e))


    elif mode == "Login":
        st.subheader("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login", key="login_button"):
            if authenticate_user(username, password):
                st.success(f"Welcome back, {username}!")
                st.session_state["username"] = username
            else:
                st.error("Invalid username or password.")
