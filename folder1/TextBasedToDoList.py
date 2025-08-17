tasks = []

def addTask():
    task = input("Enter the task:  ")
    tasks.append(task)
    print(f"Task {task} added to the list")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed")
        else:
            print(f"Task {taskToDelete} was not found.")
    except:
        print("Invalid input")

def listTasks():
    if not tasks:
        print("The tasks list is empty")
    else:
        print("Current tasks")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

print("------------------------------")
print("Welcome to Text-Based ToDoList")
print("------------------------------")


while True:
    print("--------------------------------------")
    print("Please select Any one of the following")
    print("--------------------------------------")

    print("1 : Add task")
    print("2 : Delete task")
    print("3 : List task")
    print("4 : Quit")

    n = input("Enter a input: ")
    match(n):
        case "1":
            addTask()
            print("Task added successfully")
            #break
        case "2":
            deleteTask()
            print("Task deleted successfully")
            #break
        case "3":
            listTasks()
            print("Number of tasks are listed")
            #break
        case "4":
            print("exited")
            break
