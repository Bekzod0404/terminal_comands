import os

while True:
    command = input("Input commands (ls, touch, mkdir, cd, \\q): ")

    if command == "ls":
        files = os.listdir()
        print("Files: ", files)

    elif command == "touch":
        file_name = input("Input file name: ")
        file_content = input(f"{file_name} input writing content: ")

        with open(file_name, 'w') as file:
            file.write(file_content)

        print(f"{file_name} created and {file_content} written.")

    elif command == "mkdir":
        folder_name = input("Input folder name: ")
        os.mkdir(folder_name)
        print(f"{folder_name} folder opened.")

    elif command == "cd":
        destination = input("Input name of the destination folder: ")
        if destination == "..":
            os.chdir(os.path.dirname(os.getcwd()))
        else:
            os.chdir(destination)
        print(f"changed directory to {destination}")

    elif command == "\\q":
        print("Quiting...")
        break

    else:
        print("Wrong command!, try again.")