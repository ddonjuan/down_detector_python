import socket
import subprocess
import platform

def user_ip_address():
    user_ip = socket.gethostbyname(socket.gethostname())
    return user_ip
