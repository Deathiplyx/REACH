# this code is used to open a browser and to keep trying for a while until it sees a browser is opened successfully.

import webbrowser
def run():
    webbrowser.open("https://www.google.com")
    #check if browser is opened successfully
    import time
    for _ in range(10):
        time.sleep(1)
        # check if browser is opened successfully
        import psutil
        browser_processes = [proc for proc in psutil.process_iter(['name']) if proc.info['name'] and ('chrome' in proc.info['name'].lower() or 'brave' in proc.info['name'].lower() or 'edge' in proc.info['name'].lower() or 'firefox' in proc.info['name'].lower() or 'opera' in proc.info['name'].lower())]
        if browser_processes:
            print("Browser is opened successfully.")
            return True
    print("Failed to open browser after multiple attempts.")
    return False
# this code opens google on 'any' web browser, and you will instantly be on the google search bar