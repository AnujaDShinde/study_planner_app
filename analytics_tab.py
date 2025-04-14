import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import get_tasks_for_user


def analytics_tab():
    st.title("📊 Task Analytics")

    if "username" not in st.session_state:
        st.warning("Please log in to view analytics.")
        return

    username = st.session_state["username"]
    tasks = get_tasks_for_user(username)

    if not tasks:
        st.info("No tasks found to analyze.")
        return

    # Convert to DataFrame
    df = pd.DataFrame(tasks, columns=["ID", "Task", "Due Date", "Status"])

    # Status distribution
    status_counts = df["Status"].value_counts()
    st.subheader("Task Status Distribution")
    fig1, ax1 = plt.subplots()
    ax1.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)

    # Tasks per day
    df["Due Date"] = pd.to_datetime(df["Due Date"])
    task_per_day = df.groupby(df["Due Date"].dt.date).size()
    st.subheader("Tasks Per Day")
    st.bar_chart(task_per_day)

    # Status bar chart
    st.subheader("Status Breakdown")
    st.bar_chart(status_counts)
