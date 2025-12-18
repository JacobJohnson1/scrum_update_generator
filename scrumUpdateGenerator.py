import os
import re
from datetime import datetime, timedelta

def get_previous_weekday(date):
    """Return the previous weekday (Monday-Friday) before the given date."""
    previous_day = date - timedelta(days=1)
    while previous_day.weekday() >= 5:
        previous_day -= timedelta(days=1)
    return previous_day

# Get dates
today = datetime.today()
previous_weekday = get_previous_weekday(today)
today_str = today.strftime("%m-%d")
prev_str = previous_weekday.strftime("%m-%d")

# File name based on today's date
file_name = f"scrumUpdate{today_str}.txt"
prev_file = f"scrumUpdate{prev_str}.txt"
desktop_path = os.path.join(os.path.expanduser("C:/Users/jjohnso1/OneDrive - Missouri Employers Mutual Ins/Desktop"))
file_name = os.path.join(desktop_path, f"scrumUpdate{today_str}.txt")

# Updates/Blockers
yesterdaysUpdate = "- work done from yesterday\n- and another line from yesterday"
todaysUpdate = "- scrum update for today\n- line 2"
blockers = "- here's what's holding me up"

# Write to file
with open(file_name, "w") as file:
    file.write(f"Yesterday: ({prev_str})\n")
    file.write(f"{yesterdaysUpdate} \n")
    file.write(f"\nToday: ({today_str})\n")
    file.write(f"{todaysUpdate} \n")
    file.write(f"\nBlockers: \n")
    file.write(f"{blockers} \n")
    
# Delete previous weekday's file if it exists
if os.path.exists(prev_file):
    os.remove(prev_file)
    print(f"Deleted previous file: {prev_file}")

# still working on this stuff to delete all previous files
# pattern = re.compile(r"^scrumUpdate\d+$")

# for filename in os.path(desktop_path):  # or a specific directory
#     if pattern.match(filename):
#         filepath = os.path.join(".", filename)
#         if os.path.exists(filepath):
#             os.remove(filepath)
#             print(f"Deleted previous file: {filepath}")
# else:
#     print(f"No previous file(s) to delete.")