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


print("__     __    _         ___")
print("\ \   / /_ _| | __ _  |_ _|_ __")
print(" \ \ / / _` | |/ _` |  | || '_ \")
print("  \ V / (_| | | (_| |  | || |_) |")
print("   \_/ \__, |_|\__,_| |___| .__/")
print("       |___/              |_|")
                                                 
                                                  
                                                    
print
print "Vgla DDoS - Made By Vgla"
print "YouTube: https://www.youtube.com/@VglaRat"
print "GitHub: https://github.com/Vgla7"
print 
print "Descobrir Ip Do Site"
print "Coloque Apenas O Nome Do Site E O Sufixo"
print
ip = raw_input("Nome Do Site: ")

os.system("clear")
print "[                    ] 0% "
time.sleep(1)
os.system("clear")
print "[=====               ] 25%"
time.sleep(1)
os.system("clear")
print "[==========          ] 50%"
time.sleep(1)
os.system("clear")
print "[===============     ] 75%"
time.sleep(1)
os.system("clear")
print "[====================] 100%"
time.sleep(1)
vgla = "ping " + ip
os.system("clear")
os.system(vgla)
