import os
import glob
# import subprocess

def get_usb_exe_paths():
    # Get the path of the USB drive


    # usb_drive = "C://Users/FelixLUI/autoInstaller/Installer" UAT
    usb_drive = "D://autoInstaller/Installer"
    print("Install files path"+usb_drive)

    # Construct the search pattern to find .exe files in the USB drive
    search_pattern = os.path.join(usb_drive, "*.exe")

    # Find all .exe files in the USB drive
    exe_paths = glob.glob(search_pattern)

    return exe_paths

def set_user_password():
    # # username = input("Enter your username: ")
    username = "User"
    password = "Novo@1234"
    # os.system("net user " + username +" "+ password)
    # print("net user " + username +" "+ password)
    os.system("net user " + username +" "+ password + " /add")
    print("net user " + username +" "+ password + " /add")

# Prompt the user to set the password
set_password = input("Do you want to set a new User? (y/n): ")
if set_password.lower() == "y":
    set_user_password()

# Get the paths of .exe files in the USB drive
exe_paths = get_usb_exe_paths()

# Print the paths of the .exe files
for path in exe_paths:
    print(path)
    os.startfile(path)



