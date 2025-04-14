from datetime import datetime, timedelta
from database import get_tasks_for_user, save_study_plan

def auto_generate_study_plan(username):
    tasks = get_tasks_for_user(username)
    today = datetime.today().date()
    plan = []

    for i, task in enumerate(tasks):
        due_date = datetime.strptime(task[4], "%Y-%m-%d").date()
        days_left = (due_date - today).days
        if days_left < 1:
            continue
        plan_date = today + timedelta(days=i % days_left)
        plan.append((username, task[2], plan_date.strftime("%Y-%m-%d")))

    save_study_plan(username, plan)
    return plan