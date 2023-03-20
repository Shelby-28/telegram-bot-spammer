import requests
import time
import os
os.system("clear")
print('''
\033[1;36m
██╗░░░██╗███████╗░░░░░░░░███╗░░██████╗░
╚██╗░██╔╝██╔════╝░░░░░░░████║░░╚════██╗
░╚████╔╝░█████╗░░█████╗██╔██║░░░░███╔═╝
░░╚██╔╝░░██╔══╝░░╚════╝╚═╝██║░░██╔══╝░░
░░░██║░░░██║░░░░░░░░░░░███████╗███████╗
░░░╚═╝░░░╚═╝░░░░░░░░░░░╚══════╝╚══════╝\n
\x1b[0m
YF-12'S A TELEGRAM STICKER SPAMMER FOR GROUP CHAT
Telegram : @TheShelbyOne 
Version : 2.5
''')

token = input("[*] BOT TOKEN: ") 
NM = input("[*] NUMBER OF MESSAGES: ") 
id = input("[*] ENTER CHAT ID: ")
Sticker_id = input("[*] ENTER STICKER ID: ")
sleept = input("[*] ENTER SLEEP TIME: ")

is_topic = input("[*] Does the group have topics(Y/N)? ").lower()
if is_topic == 'y':
    thread_id = input("[*] Enter Message Thread ID: ")
elif is_topic == 'n':
    pass
else:
    print("INVALID !")
    
print("\n\033[1;36mIF THE MESSAGES DELAYS\nTHAT'S BECAUSE TELEGRAM API HAS COOLDOWN !\x1b[0m\n")


    
for i in range(0,int(NM)):
    if is_topic == 'y':      
    
        telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendSticker?chat_id={id}&sticker={Sticker_id}&message_thread_id={thread_id}')
        print(str(i+1)+"-Sent")
        time.sleep(float(sleept))
        
    elif is_topic == 'n':
    
        telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendSticker?chat_id={id}&sticker={Sticker_id}&message_thread_id={thread_id}')
        print(str(i+1)+"-Sent")
        time.sleep(float(sleept))
        
    else:
        print("INVALID !")
