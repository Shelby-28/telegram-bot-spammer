import requests
import time
import os
os.system("clear")
print('''
\033[1;36m
███╗░░░███╗██╗░██████╗░░░░░░░██████╗░███████╗
████╗░████║██║██╔════╝░░░░░░░╚════██╗██╔════╝
██╔████╔██║██║██║░░██╗░█████╗░░███╔═╝██████╗░
██║╚██╔╝██║██║██║░░╚██╗╚════╝██╔══╝░░╚════██╗
██║░╚═╝░██║██║╚██████╔╝░░░░░░███████╗██████╔╝
╚═╝░░░░░╚═╝╚═╝░╚═════╝░░░░░░░╚══════╝╚═════╝░\n
\x1b[0m
MiG-25'S A TELEGRAM MASSAGE SPAMMER FOR GROUP CHAT
Telegram : @TheShelbyOne 
VERSION : 2.5
''')

token = input("[*] BOT TOKEN: ")
MSG = input("[*] ENTER THE MESSAGE: ")
NM = input("[*] NUMBER OF MESSAGES: ")
SLEEPT= input("[*] SLEEP TIME: ")
ID = input("[*] CHAT ID: ")

is_topic = input("[*] Does the group have topics(Y/N)? ").lower()
if is_topic == 'y':
    thread_id = input("[*] Enter Message Thread ID: ")
elif is_topic == 'n':
    pass
else:
    print("INVALID !")

print("\n\033[1;36mIF THE MESSAGES DELAYS\nTHAT'S BECAUSE TELEGRAM API HAS COOLDOWN !\x1b[0m\n")

for i in range(0,int(NM)):
    if is_topic =='y':
        telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={MSG}&message_thread_id={thread_id}')
        print(str(i+1)+"-Sent")
        time.sleep(float(SLEEPT))
    
    
    elif is_topic =='n':
        telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={MSG}')
        print(str(i+1)+"-Sent")
        time.sleep(float(SLEEPT))
    else:
        print("INVALID !")
    
    
