import streamlit as st
from fpdf import FPDF
from database import get_tasks_for_user

def export_pdf_page():
    st.title("📤 Export Tasks to PDF")

    username = st.session_state.get("username", None)
    if not username:
        st.warning("⚠️ Please log in to export your tasks.")
        return

    tasks = get_tasks_for_user(username)
    if not tasks:
        st.info("ℹ️ You have no tasks to export.")
        return

    if st.button("Generate PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt=f"Study Tasks for {username}", ln=True, align="C")
        pdf.ln(10)

        for task in tasks:
            task_id, task_name, due_date, status = task
            line = f"📌 Task: {task_name} | 📅 Due: {due_date} | 🔄 Status: {status}"
            pdf.multi_cell(0, 10, txt=line)

        filename = f"{username}_tasks.pdf"
        pdf.output(filename)

        st.success("✅ PDF generated successfully.")
        with open(filename, "rb") as f:
            st.download_button("📥 Download PDF", f, file_name=filename, mime="application/pdf")
