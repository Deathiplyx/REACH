# this script is used to open an application with a specific name, using our premade code in the atoms folder

application_name = "notepad.exe"  # Change this to the name of the application you want to open

def run(application_name):
    import time
    import psutil
    import subprocess
    subprocess.Popen(application_name)
    while True:
        # Check if the application is running
        if any(application_name in proc.name() for proc in psutil.process_iter()):
            print(f"{application_name} is now open.")
            break
        time.sleep(1)  # Wait for 1 second before checking again


run(application_name)