##Create that ask user to enter n no of todo and display it.
todos =[]
total_todo = input=("Entar total number of todo: ")
for i in range(1,total_todo+1):
    todo = input(f"Enter to do {i}:")
    todos.append(todo)##append add
    print("\n............\n")
    print("All todos are : ")
    #Display all result
    for todo in todos:
        print(todo)