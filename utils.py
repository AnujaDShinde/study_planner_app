from datetime import datetime

def format_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")
    except:
        return date_str


# utils.py
def get_status_color(status):
    """Returns a color for the task status."""
    if status == 'Pending':
        return 'yellow'
    elif status == 'In Progress':
        return 'blue'
    elif status == 'Completed':
        return 'green'
    return 'gray'  # Default color for undefined statuses

