import streamlit as st
from database import add_user, authenticate_user
from utils import is_valid_email, is_strong_password

def main():
    st.title("📝 Sign Up / Login")

    menu = ["Login", "Sign Up"]
    choice = st.selectbox("Choose Option", menu)

    if choice == "Sign Up":
        st.subheader("Create New Account")

        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        role = st.selectbox("Role", ["student", "teacher"])

        if st.button("Register"):
            # Basic validations
            if not username or not email or not password or not confirm_password:
                st.error("Please fill in all fields.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif not is_valid_email(email):
                st.error("Invalid email format.")
            elif not is_strong_password(password):
                st.warning("Password should be at least 6 characters and include letters and numbers.")
            else:
                add_user(username, password, role)
                st.success(f"Account created for {username} ✅")
                st.info("Go to Login to access your dashboard.")

    elif choice == "Login":
        st.subheader("Login to Your Account")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state["username"] = username
                st.success(f"Welcome, {username} 🎉")
                st.session_state["page"] = "Dashboard"
            else:
                st.error("Invalid username or password.")
