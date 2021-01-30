import socket
import subprocess
import platform


# grabs users IP Address
def user_ip_address():
    user_ip = socket.gethostbyname(socket.gethostname())
    return user_ip


'''
**Function will take any IP4 Address and ping it to see if we can get a response
**Returns True if IP Address is active, False if there is no response
'''
def ping_ip(ip_address):
    try:
        ping_ip = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', ip_address), shell=True, universal_newlines=True)

        if 'unreachable' in ping_ip:
            return False
        else:
            return True

    except Exception:
        return False
