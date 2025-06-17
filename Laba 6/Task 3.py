from datetime import datetime

class Task:
    def __init__(self, date_start, date_finish, description):
        self.date_start = date_start
        self.date_finish = date_finish
        self.description = description

tasks = [
    Task("2025-01-01", "2025-01-05", "Job 1"),
    Task("2025-02-03", "2025-02-07", "Job 2"),
    Task("2025-03-28", "2025-03-30", "Job 3"),
    Task("2025-05-05", "2025-05-09", "Job 4"),
    Task("2025-05-06", "2025-05-09", "Job 5"),
]

latest_task = tasks[0]
for task in tasks:
    if datetime.strptime(task.date_finish, "%Y-%m-%d") > datetime.strptime(latest_task.date_finish, "%Y-%m-%d"):
        latest_task = task

print(f"Start - {latest_task.date_start}, Finish - {latest_task.date_finish}, Description - {latest_task.description}")