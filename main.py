import pandas as pd
import os

df = pd.DataFrame(columns=['name', 'date', 'status'])

filename = "tasks.csv"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, filename)


def menu(): 
    global df
    df = pd.read_csv("tasks.csv")
    if df.empty:
        new_task()
    else :
        print("go")
        main_menu()


def main_menu():
    while True:
        print("\nWhat do you want to do?")
        print("1 - Add a task")
        print("2 - Modify a task")
        print("3 - Delete a task")
        print("4 - Show tasks")
        print("0 - Exit")
        
        choice = input("Enter your choice: ").strip()
        
        action = menu_options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")




def get_option():
    while True:
        choice = input("Is it done? (done / not done): ").strip().lower()
        if choice in ["done", "not done"]:
            return choice
        else:
            print("Invalid input. Please enter only 'done' or 'not done'.")

def new_task():
    global df
    num = int(input("How many tasks do you want to add? "))
    for i in range(num):
        print(f"\nTask {i+1}")
        adding()
    print("\nNew task list:")
    print(df)
    df.to_csv(file_path, index=False)
    

def adding():
    global df
    name = input("What is the task name? ")
    date = input("What is the task date? ")
    status = get_option()
    df.loc[len(df)] = [name, date, status]
    return df

def modify_task():
    print(df)
    num=input("what the task that you want to change ?:")
    df.loc[num, 'name'] = input('What is the task name?')
    df.loc[num, 'date'] = input('What is the task date?')
    df.loc[num, 'status'] = get_option()
    return df

def show_tasks():
    print(df)
    see=input('what task you want to check')
    return print(df.loc[see])


def delete_task():
    print(df)
    delet=input('what the task you want to delet')
    df.drop(index=delet, inplace=True)
    return df

def exte_task() :
    df = pd.read_csv(file_path)
    if df.empty:
        print("The list is empty. Creating a new task list...")
        new_task()
    else:
        print("This list is not empty. chose")
        menu()

def save_tasks():
    df.to_csv(file_path, index=False)
    

menu_options = {
    "1": adding,
    "2": modify_task,
    "3": delete_task,
    "4": show_tasks,
}
if not os.path.exists(file_path):
    print("CSV file not found. Creating a new one...")
    # Create an empty DataFrame with the right columns
    df = pd.DataFrame(columns=['name', 'date', 'status'])
    df.to_csv(file_path, index=False)
    exte_task()
    save_tasks()
else:
    exte_task()
    save_tasks()
