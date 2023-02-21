import requests
import time

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
VERSION : 2.0
''')

token = input("[+] BOT TOKEN: ") 
MSG = input("[+] ENTER THE MESSAGE: ")
NM = input("[+] NUMBER OF MESSAGES: ")
SLEEPT= input("[+] SLEEP TIME: ")
ID = input("[+] CHAT ID: ")

i=0
while i<int(NM):
    telegram_msg = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={MSG}')
    print(str(i+1)+"-Sent")
    i+=1
    time.sleep(float(SLEEPT))
    
    
