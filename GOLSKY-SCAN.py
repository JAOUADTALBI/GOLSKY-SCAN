from colorit import *
import subprocess
import nmap
import os
import threading
from six.moves import input 
import sys
import requests

# Colors code
ORANGE = 255, 165, 0
GREEN = 0, 255, 0
RED = 255, 0, 0
YELLOW = 255, 255, 0
PURPLE = 148, 0, 211

DEEPPINK = 255, 20, 147
CYAN = 0, 238, 238
WHITE = 255, 255, 255

init_colorit()

print(color("""



  /$$$$$$   /$$$$$$  /$$        /$$$$$$  /$$   /$$/$$     /$$        /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$
 /$$__  $$ /$$__  $$| $$       /$$__  $$| $$  /$$/  $$   /$$/       /$$__  $$ /$$__  $$ /$$__  $$| $$$ | $$
| $$  \__/| $$  \ $$| $$      | $$  \__/| $$ /$$/ \  $$ /$$/       | $$  \__/| $$  \__/| $$  \ $$| $$$$| $$
| $$ /$$$$| $$  | $$| $$      |  $$$$$$ | $$$$$/   \  $$$$/        |  $$$$$$ | $$      | $$$$$$$$| $$ $$ $$
| $$|_  $$| $$  | $$| $$       \____  $$| $$  $$    \  $$/          \____  $$| $$      | $$__  $$| $$  $$$$
| $$  \ $$| $$  | $$| $$       /$$  \ $$| $$\  $$    | $$           /$$  \ $$| $$    $$| $$  | $$| $$\  $$$
|  $$$$$$/|  $$$$$$/| $$$$$$$$|  $$$$$$/| $$ \  $$   | $$          |  $$$$$$/|  $$$$$$/| $$  | $$| $$ \  $$
 \______/  \______/ |________/ \______/ |__/  \__/   |__/           \______/  \______/ |__/  |__/|__/  \__/


        By: GOLSKY                                            

 """,(WHITE)))


host = input(color("[#]", GREEN) + color(" Enter IP Cible: ", GREEN))
print(color("|", CYAN) + color("  1):", WHITE) + color(" All                                                                      ", ORANGE) + color("|", CYAN))
print(color("|", CYAN) + color("  2):", WHITE) + color(" Scan Port & Vulnerability                                                ", ORANGE) + color("|", CYAN))
print(color("|", CYAN) + color("  3):", WHITE) + color(" Directory Bruteforcing  - Hidden Files & Directories                     ", ORANGE) + color("|", CYAN))
print(color("|", CYAN) + color("  4):", WHITE) + color(" Exploitation Vulnerability                                               ", ORANGE) + color("|", CYAN))

# Tools scan port
def scan(host):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host, '1-65535')
    for host in nm_scan.all_hosts():
        for proto in nm_scan[host].all_protocols():
            lport = nm_scan[host][proto].keys()
            for port in lport:
                if nm_scan[host][proto][port]['state'] == 'open':
                    print(color(f"Open ", WHITE) + color(f'{host}:{port} ', PURPLE) +
                          color(">", WHITE) + color(f' {nm_scan[host][proto][port]["name"]}', PURPLE))


# Command nmap details
def scan2():
    command = f'nmap -p- -T4 --script vuln -oN {host}.txt {host}'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode())
    print(result.stderr.decode())


# Brute force directory
def scan3():
    f = open("shdscan.txt")
    x = "http://" + host + "/"
    direc = f.readlines()
    try:
        for d in direc:
            target2 = (x + d).rstrip()
            r = requests.get(target2)
            if r.status_code == 200:
                print(color(" [$] ", WHITE) + color(f'{target2}', PURPLE) + " > " + color(f'{r.status_code}', WHITE))
    except requests.exceptions.ConnectionError:
        print("Server is down!!!\rPlease run Apache server!!")


# ------------------------
xss = int(input(color("-->", GREEN) + color(" Enter Number What Do you Need: ", GREEN)))

# All
if xss == 1:
    print(color("[>]", GREEN) + color(" Wait For Enumeration Scanning...\n", ORANGE))
    t1 = threading.Thread(target=scan, args=(host,))
    print("\r")
    print(color("[>]", GREEN) + color(" Script to be run Some brute Force Directory...\n", ORANGE))
    t3 = threading.Thread(target=scan3)
    print("\r")
    print(color("[>]", GREEN) + color(" Script to be run Some Show details For All Port...\n", ORANGE))
    t2 = threading.Thread(target=scan2)
    t1.start()
    t3.start()
    t2.start()

# Scan-Port
elif xss == 2:
    print(color("[>]", GREEN) + color(" Wait For Enumeration Scanning...\n", ORANGE))
    t1 = threading.Thread(target=scan, args=(host,))
    print("\r")
    print(color("[>]", GREEN) + color(" Script to be run Some Show details For All Port...\n", ORANGE))
    t2 = threading.Thread(target=scan2)
    t1.start()
    t2.start()

# Brute Forcing Directory
elif xss == 3:
    print(color("[>]", GREEN) + color(" Script to be run Some brute Force Directory...\n", ORANGE))
    t3 = threading.Thread(target=scan3)
    t3.start()
