tasks = []

while True:
    print("--- TO-DO LIST MENU ---")
    print("• Add a task")
    print("• Remove a task")
    print("• View tasks")
    print("• Exit")

    print("If you want to add a task use commas to separate them.")
    choice = input("Choose an option: ")


    if choice == "add task":
        task_input = input("Enter task(s): ")

        for task in task_input.split(","):        # # go through each task in the list one at a time
            tasks.append(task.strip())   # adds each task to the end of the list
        print("Task(s) added!")

    elif choice == "remove task":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("Here are your tasks:")
            number = 1
            for task in tasks:
                print(number, task)
                number = number + 1

            number_to_remove = int(input("Enter the task number to delete: "))
            tasks.pop(number_to_remove - 1)   # delete the chosen task from the list
            print("Task removed!")
            print("Here are your remaining tasks:")
            number = 1
            for task in tasks:
                print(number, task)
                number = number + 1


    elif choice == "view tasks":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            number = 1
            for task in tasks:
                print(number, task)
                number = number + 1

    elif choice == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")