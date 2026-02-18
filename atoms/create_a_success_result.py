# this script is designed to give a message if it recieves the input any input other than fail, but if it does recieve fail it does nothing
def run(input):
    if input != 'fail':
        print("Success! The command was recognized and executed.")
    else:
        pass