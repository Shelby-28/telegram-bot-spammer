import requests
import time
print('''
\033[1;36m
██████╗░░░░░░░███████╗██████╗░
██╔══██╗░░░░░░██╔════╝╚════██╗
██████╦╝█████╗██████╗░░░███╔═╝
██╔══██╗╚════╝╚════██╗██╔══╝░░
██████╦╝░░░░░░██████╔╝███████╗
╚═════╝░░░░░░░╚═════╝░╚══════╝\n

\x1b[0m
B-52'S A TELEGRAM PHOTO SPAMMER FOR GROUP CHAT
Telegram : @TheShelbyOne 
VERSION : 2.1
''')
token = input("[+] BOT TOKEN: ") 
NM = input("[+] NUMBER OF MESSAGES: ") 
id = input("[+] ENTER CHAT ID: ")
message = input("[+] ENTER MESSAGE: ")
img = input("[+] ENTER IMAGE URL: ")
sleept = input("[+] ENTER SLEEP TIME: ")

print("\n\033[1;36mIF THE MESSAGES DELAYS\nTHAT'S BECAUSE TELEGRAM API HAS COOLDOWN !\x1b[0m\n")


    
i=0
while i<int(NM):
                                    
    telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={id}&caption={message}&photo={img}')
    print(str(i+1)+"-Sent")
    i+=1
    time.sleep(float(sleept))