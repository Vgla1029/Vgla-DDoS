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


print " _____ _____ __    _____    ____  ____      _____ "
print "|  |  |   __|  |  |  _  |  |    \|    \ ___|   __|"
print "|  |  |  |  |  |__|     |  |  |  |  |  | . |__   |"
print " \___/|_____|_____|__|__|  |____/|____/|___|_____|"
                                                    
                                                    
print
print "Vgla DDoS - Made By Vgla"
print "YouTube: https://www.youtube.com/@VglaRat"
print "GitHub: https://github.com/Vgla7"
print 
print "Descobrir Ip Do Site!"
print "(não coloque HTTPS, WWW ou HTTP)"
print
ip = raw_input("Nome Do Site: ")

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
os.system("ping" ip)
