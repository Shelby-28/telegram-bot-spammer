import requests
import time

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
Version : 2.0
''')

token = input("[+] BOT TOKEN: ") 
NM = input("[+] NUMBER OF MESSAGES: ") 
id = input("[+] ENTER CHAT ID: ")
Sticker_id = input("[+] ENTER STICKER ID: ")
sleept = input("[+] ENTER SLEEP TIME: ")

print("\n\033[1;36mIF THE MESSAGES DELAYS\nTHAT'S BECAUSE TELEGRAM API HAS COOLDOWN !\x1b[0m\n")


    
i=0
while i<int(NM):
    telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendSticker?chat_id={id}&sticker={Sticker_id}')
    print(str(i+1)+"-Sent")
    i+=1
    time.sleep(float(sleept))








#-1001794561485 
#CAADAgADOQADfyesDlKEqOOd72VKAg
