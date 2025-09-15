"""Turns out strftime('%s) only works on Unix. Try running with WSL if it doesn't work. 
Also, the datetime library took a while to get working, so I wasn't able to commit when I wanted to.
I originally wanted a nicer UI, which captured the keyboard inputs and navigated with arrow keys and enter, 
but did not want to have to learn a second library. """

import datetime
tasks = []

def get_due_date():
    """Get the due date for the task from the user"""
    while True:
        print("Please type in the date, month and year the task is due.")
        try:
            due_day = int(input("Due Day: "))
            due_month = int(input("Due Month: "))
            due_year = int(input("Due Year: "))
            due_date = datetime.datetime(due_year, due_month, due_day)
            break
        except ValueError:
            print("Date must be valid integer between 1 and 31.")
    return due_date

def return_due_date(task):
    """returns the task due date as a unix timestamp for sorting"""
    return(task[1].strftime('%s'))

def add_task():
    """Add a task to the list of tasks"""
    tasks.append([input("Task name: "), get_due_date()])
    tasks.sort(key = return_due_date)
    print(tasks)



def display_all_tasks(tasks):
    """Prints each task and its due date in a human-readable format"""
    for name, due in tasks:
        print(f"{name}, due {due.strftime('%c')}")
    
def check_earliest_task():
    """prints the first task in the list, which is the earliest"""
    print(f"Earliest task is {[tasks[0][0]]}, due on {tasks[0][1].strftime('%c')}")

def complete_earliest_task(tasks):
    """Marks the earliest task as complete, by deleting it. Then calls display_all_tasks."""
    earliest_task = tasks[0][0]
    tasks.pop(0)
    print(f"Removed {earliest_task}, remaining tasks:")
    display_all_tasks(tasks)

###################

def menu():
    """Main menu function"""
    while True:
        try:
            print("""What would you like to do? (1-5)
            1. Add a task
            2. Display tasks
            3. Check the earliest due task
            4. Mark earliest due task as complete
            5. Quit""")
            menu_selection = int(input("> "))
            if menu_selection >= 6:
                print("Please choose options 1-5")
            elif menu_selection <= 0:
                print("Please choose options 1-5")
            elif menu_selection == 1:
                add_task()
            elif menu_selection == 2:
                display_all_tasks(tasks)
            elif menu_selection == 3:
                check_earliest_task()
            elif menu_selection == 4:
                complete_earliest_task(tasks)
            elif menu_selection == 5:
                exit()
        except ValueError:
            print("Please choose options 1-5.")
menu()