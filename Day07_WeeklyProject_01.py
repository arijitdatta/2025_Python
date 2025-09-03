#At the start of the day you have a checklist The tasks which you were able to finish, should get added to completed_tasks The tasks which you were not able to finish, should get added to incomplete_tasks This project is about organizing your daily tasks into two categories: completed tasks and incomplete tasks. Here’s how it works: 1. At the start of the day, you create a checklist of tasks you want to accomplish. 2. At the end of the day, you review which tasks you could finish and which you couldn’t. – If a task is finished, you move it to the completed tasks list. – If a task is not finished, you move it to the incomplete tasks list. This way, by the end of each day, you’ll have a clear overview of what you completed and what still needs attention.
#

#Initialize lists for completed and incomplete tasks
completed_tasks = []
incomplete_tasks = []

#Start of the day checklist
day_tasks = ["Task 1", "Task 2", "Task 3"]

#Take user input for completed tasks
print("Today's tasks:", day_tasks)
for task in day_tasks:
    status = input(f"Did you complete '{task}'? (y/n): ").strip().lower()
    if status == 'y':
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("Completed tasks:", completed_tasks)
print("Incomplete tasks:", incomplete_tasks)