from down_detector_functions.ip_address_functions import user_ip_address


#function that executes the program
def run_down_detector():
    print("Program running....")
    user_ip = user_ip_address()
    print("Your IP Address: ", user_ip)

if __name__ == '__main__':
    run_down_detector()


