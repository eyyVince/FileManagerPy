import sys
import os
import shutil
import send2trash

print('Welcome to the python-file-manager\n')

drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

def listDirectories():
    for x in os.listdir(os.getcwd()):
        print(x)

def confirm_action(message):
    ans = input(message + " (YES/NO): ").lower()
    return ans in ['yes', 'y']

while True:
    print("\n1.Open files/folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n5.Delete\n")
    result = input("Choose one of the following: ")

    # ================= OPEN =================
    if result == '1':
        print('\nQuick Access:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')

        print('Drives:')
        for x in drives:
            print(x)

        while True:
            inp = input("\nEnter your Choice: ")

            paths = {
                '1': 'C:\\Users\\%USERNAME%\\Documents',
                '2': 'C:\\Users\\%USERNAME%\\Videos',
                '3': 'C:\\Users\\%USERNAME%\\Pictures',
                '4': 'C:\\Users\\%USERNAME%\\Downloads'
            }

            if inp in paths:
                os.chdir(os.path.expandvars(paths[inp]))
                break
            elif inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Invalid input.')

        while True:
            listDirectories()
            print('\nType "exitManager" to exit.')
            print('Type "backManager" to go back.')

            res = input('\nChoose a file/folder: ')

            if res in os.listdir():
                if os.path.isfile(res):
                    os.system(f'"{res}"')
                else:
                    os.chdir(res)
            elif res == 'exitManager':
                sys.exit(0)
            elif res == 'backManager':
                os.chdir('..')
            else:
                print('Not found.')

    # ================= RENAME =================
    elif result == '2':
        print('Drives:')
        for x in drives:
            print(x)

        while True:
            inp = input("\nEnter drive: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Invalid.')

        while True:
            listDirectories()
            print('\nType "renameManager" to rename current folder')

            res = input('\nChoose file/folder: ')

            if res in os.listdir():
                new_name = input("New name: ")
                shutil.move(res, new_name)

            elif res == 'renameManager':
                new_name = input("New name: ")
                current = os.getcwd()
                os.chdir('..')
                shutil.move(current, new_name)

            elif res == 'backManager':
                os.chdir('..')

            elif res == 'exitManager':
                sys.exit(0)

    # ================= MOVE =================
    elif result == '3':
        print("Move files")

        while True:
            for x in drives:
                print(x)

            inp = input("\nEnter drive: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break

        while True:
            listDirectories()
            res = input('\nSelect file to move: ')

            if res in os.listdir() and os.path.isfile(res):
                source = os.path.join(os.getcwd(), res)

                print("Choose destination drive:")
                for x in drives:
                    print(x)

                dest_drive = input("Drive: ")
                if dest_drive in drives:
                    os.chdir(dest_drive + '\\')

                    listDirectories()
                    folder = input("Select destination folder: ")

                    if folder in os.listdir() and os.path.isdir(folder):
                        shutil.move(source, os.path.join(os.getcwd(), folder))
                        print("Moved successfully")

            elif res == 'backManager':
                os.chdir('..')

            elif res == 'exitManager':
                sys.exit(0)

    # ================= COPY =================
    elif result == '4':
        print("Copy files")

        while True:
            for x in drives:
                print(x)

            inp = input("\nEnter drive: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break

        while True:
            listDirectories()
            res = input('\nSelect file to copy: ')

            if res in os.listdir() and os.path.isfile(res):
                source = os.path.join(os.getcwd(), res)

                print("Choose destination drive:")
                for x in drives:
                    print(x)

                dest_drive = input("Drive: ")
                if dest_drive in drives:
                    os.chdir(dest_drive + '\\')

                    listDirectories()
                    folder = input("Select destination folder: ")

                    if folder in os.listdir() and os.path.isdir(folder):
                        shutil.copy(source, os.path.join(os.getcwd(), folder))
                        print("Copied successfully")

            elif res == 'backManager':
                os.chdir('..')

            elif res == 'exitManager':
                sys.exit(0)

    # ================= DELETE =================
    elif result == '5':
        print("\n1. Permanent\n2. Recycle Bin")
        choice = input("Choose delete type: ")

        while True:
            for x in drives:
                print(x)

            inp = input("Select drive: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break

        while True:
            listDirectories()
            res = input("\nSelect file/folder: ")

            if res in os.listdir():
                if confirm_action("Are you sure you want to delete?"):

                    if choice == '1':
                        if os.path.isfile(res):
                            os.remove(res)
                        else:
                            shutil.rmtree(res)

                    elif choice == '2':
                        send2trash.send2trash(res)

                    print("Deleted successfully")

            elif res == 'backManager':
                os.chdir('..')

            elif res == 'exitManager':
                sys.exit(0)
