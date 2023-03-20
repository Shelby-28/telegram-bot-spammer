import requests
import os
import time
os.system("clear")

print('''
\033[1;36m
███████╗░░░░░░██████╗░███████╗
██╔════╝░░░░░░╚════██╗██╔════╝
█████╗░░█████╗░█████╔╝██████╗░
██╔══╝░░╚════╝░╚═══██╗╚════██╗
██║░░░░░░░░░░░██████╔╝██████╔╝
╚═╝░░░░░░░░░░░╚═════╝░╚═════╝░

██╗░░░░░██╗░██████╗░██╗░░██╗████████╗██╗███╗░░██╗
██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝██║████╗░██║
██║░░░░░██║██║░░██╗░███████║░░░██║░░░██║██╔██╗██║
██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░██║██║╚████║
███████╗██║╚██████╔╝██║░░██║░░░██║░░░██║██║░╚███║
╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝\n

\x1b[0m
B-52'S A TELEGRAM Video SPAMMER FOR GROUP CHAT
Telegram : @TheShelbyOne 
VERSION : 2.5
''')
token = input("[*] BOT TOKEN: ") 
NM = input("[*] NUMBER OF MESSAGES: ") 
id = input("[*] ENTER CHAT ID: ")
message = input("[*] ENTER MESSAGE: ")
video = input("[*] ENTER VIDEO URL: ")
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
        telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendVideo?chat_id={id}&caption={message}&video={video}&message_thread_id={thread_id}')
        print(str(i+1)+"-Sent")
        time.sleep(float(sleept))
        
    elif is_topic == 'n':
    
        telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendVideo?chat_id={id}&caption={message}&video={video}')
        print(str(i+1)+"-Sent")
        time.sleep(float(sleept))
        
    else:
        print("INVALID !")