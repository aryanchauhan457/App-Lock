
while True:
    if is_app_running():
        # print("App is running")
        if password_status:
            continue
        else:
            closeapp()
            password_status = password_check()
            print(f'now it is {password_status}')

            if password_status:
                runapp()
    else:
        # print("App is not running")
        password_status = False
    time.sleep(1)