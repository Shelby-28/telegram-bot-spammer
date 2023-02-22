import os
import time
import subprocess

path = "telegram-bot-spammer"

os.system("apt update && apt -y upgrade")
os.system("pkg install git")
os.system("pkg install python")
os.system("git clone https://github.com/Shelby-28/telegram-bot-spammer")
os.chdir(path)
os.system("clear")

        
print('''\033[0;92m
███╗░░░███╗██╗░░░██╗░██████╗██╗░░░░░██╗████████╗
████╗░████║╚██╗░██╔╝██╔════╝██║░░░░░██║╚══██╔══╝
██╔████╔██║░╚████╔╝░╚█████╗░██║░░░░░██║░░░██║░░░
██║╚██╔╝██║░░╚██╔╝░░░╚═══██╗██║░░░░░██║░░░██║░░░
██║░╚═╝░██║░░░██║░░░██████╔╝███████╗██║░░░██║░░░
╚═╝░░░░░╚═╝░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░░╚═╝░░░\n
\x1b[0m''')

print("[1] Photo Spammer")
print("[2] Message Spammer")
print("[3] Sticker Spammer\n")


option = input('\033[1;36m[+] Choose ==> : \x1b[0m')

if option == '1':
    time.sleep(1)
    os.system("python B-52v2.py")
if option == '2':
    time.sleep(1)
    os.system("python MiG-25v2.py")
    
if option == '3':
    time.sleep(1)
    os.system("python YF-12v2.py")
    
else:
    print("INVALID NUMBER ! ")
    time.sleep(0.5)
    print("TRY AGAIN")