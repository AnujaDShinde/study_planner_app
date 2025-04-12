# Export study plan to PDF using fpdf
from fpdf import FPDF
import streamlit as st
from database import get_tasks_by_user

def generate_pdf():
    username = st.session_state.get("username", None)
    if not username:
        st.warning("Please log in to export your tasks.")
        return

    tasks = get_tasks_by_user(username)

    if not tasks:
        st.warning("No tasks found to export.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Study Tasks for {username}", ln=True, align="C")

    for task in tasks:
        task_name, due_date, status = task[2], task[3], task[4]
        pdf.cell(200, 10, txt=f"Task: {task_name}, Due: {due_date}, Status: {status}", ln=True)

    file_path = f"{username}_study_tasks.pdf"
    pdf.output(file_path)
    st.success("PDF generated successfully!")
    with open(file_path, "rb") as f:
        st.download_button(label="Download PDF", data=f, file_name=file_path)
