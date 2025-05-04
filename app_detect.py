import psutil
import time
import tkinter as tk
import subprocess
import keyboard

password_status = False

def detect_key_combination():

    try:
        # Wait for the key combination to be pressed
        if keyboard.is_pressed('ctrl+shift+a+p+l'):
            # Here we will open the application GUI
            # print("Pressed")
            # exit()
            pass

    except Exception as e:
        print(f"Error: {e}")

def runapp():
    # The Application User Model ID (AUMID) of the WhatsApp app
    app_name = "5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"

    # Command to launch the app
    command = f'explorer.exe shell:AppsFolder\\{app_name}'

    # Use subprocess to run the command
    subprocess.run(command, shell=True)

def closeapp():
    # Define the taskkill command to kill the Microsoft Edge process
    app_kill_command = f'taskkill /IM "WhatsApp.exe" /F'

    # Execute the command using subprocess
    subprocess.run(app_kill_command, shell=True)
    
def password_check():
    # Create a new tkinter window
    window = tk.Tk()
    window.geometry("400x200")
    # window.wm_attributes("-topmost", 1)
    # window.config(bg="#ff0000")

    # Create a label and an entry widget for the user input
    label = tk.Label(window, text="Enter password:")
    label.pack()
    entry = tk.Entry(window)
    entry.pack()

    password = '1234'
    password2 = '!@#$'
    global status
    status = '0'
    # Define a function to be called when the user clicks the button
    def get_input():
        global status
        user_input = entry.get()
        # Check if the user's input is equal to "1234"
        if user_input == password:
            # Close the tkinter window
            # print("User input:", user_input)
            status = '1'
            window.destroy()
        elif user_input == password2:
            # Close the tkinter window
            # print("User input:", user_input)
            status = '2'
            window.destroy()
        else:
            pass

    # Create a button that the user can click to submit their input
    button = tk.Button(window, text="Submit", command=get_input)
    button.pack()

    # Start the tkinter event loop
    window.mainloop()
    return status

def is_app_running():
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'WhatsApp.exe':
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
# wait = 1
while True:
    detect_key_combination()
    if is_app_running():
        # print("App is running")
        # wait = 10
        if password_status:
            continue
        else:
            closeapp()
            password_status = password_check()
            # print(f'now it is {password_status}')

            if password_status == '1':
                runapp()
            elif password_status == '2':
                runapp()
                break
    else:
        # print("App is not running")
        password_status = False
        # wait = 1
    time.sleep(1)

# password_status = password_check()
# print(f'now it is {password_status}')