print("=== My To-Do List ===")
tasks=[]
while True:
    print("\n1. Show the tasks")
    print("2. Add the task")
    print("3. Delete the task")
    print("4. Close")

    choice = input("Choose an action(1-4): ")
    if choice =="1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "2":
        task=input("Enter new task: ")
        tasks.append(task)
        print("New task added!")
    elif choice == "3":
        if len(tasks)==0:
            print("No tasks to delete.")
        else:
            print("\nYour tasks: ")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            try:
                num= int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted=tasks.pop(num -1)
                    print(f"Task '{deleted}' deleted!")
                else:
                    print("Wrong number.")
            except:
                print("Please enter a number.")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Wrong choice. Please try again.")
