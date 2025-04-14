import streamlit as st
from fpdf import FPDF
from database import get_tasks_for_user


def generate_pdf(username):
    tasks = get_tasks_for_user(username)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Study Plan for {username}", ln=True, align="C")

    for task in tasks:
        title, description, due_date, status = task[2], task[3], task[4], task[5]
        pdf.multi_cell(0, 10, txt=f"Task: {title}\nDescription: {description}\nDue Date: {due_date}\nStatus: {status}\n\n")

    output_path = f"{username}_study_plan.pdf"
    pdf.output(output_path)
    return output_path


def pdf_export_tab():
    st.title("📄 Export Tasks to PDF")
    if "username" in st.session_state:
        if st.button("Generate and Download PDF"):
            pdf_file = generate_pdf(st.session_state["username"])
            with open(pdf_file, "rb") as f:
                st.download_button(label="Download PDF", data=f, file_name=pdf_file, mime="application/pdf")
    else:
        st.warning("Please log in to export your tasks.")