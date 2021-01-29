from down_detector_functions.ip_address_functions import user_ip_address, ping_ip


#Test whether user's IP Address is active
def test_ip_ping():
    user_ip = user_ip_address()
    ping_response = ping_ip(user_ip)

    if ping_response:
        print("The IP Address has been reached: ", str(user_ip))
    else:
        print("The IP Address was unreachable: ", str(user_ip))

#function that executes the program
def run_down_detector():
    print("Program running....")
    test_ip_ping()


if __name__ == '__main__':
    run_down_detector()


