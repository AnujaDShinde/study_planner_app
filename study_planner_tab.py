import streamlit as st
from study_planner import auto_generate_study_plan
from database import get_study_plan

def study_planner_tab():
    st.title("🧠 Personalized Study Planner")
    if "username" in st.session_state:
        if st.button("Generate Study Plan"):
            auto_generate_study_plan(st.session_state["username"])
            st.success("Study plan generated!")

        study_plan = get_study_plan(st.session_state["username"])
        if study_plan:
            st.subheader("📅 Your Study Plan:")
            for item in study_plan:
                task, date = item[1], item[2]
                st.write(f"📌 **{task}** on {date}")
        else:
            st.info("Click 'Generate Study Plan' to see your plan.")
    else:
        st.warning("Please log in to view your study planner.")