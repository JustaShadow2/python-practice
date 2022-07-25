import os.path
import base64
from asyncio.windows_events import NULL


def textfilecheck():
    if os.path.exists('passwordmanager.txt'):
        NULL

    else:
        file = open('passwordmanager.txt', 'w')
        file.close
        

def appendfile():
    file = open('passwordmanager.txt', 'a')

    username = input('Input the username: ')
    password = input('Input the password: ')
    web = input('Input the web adress: ')

    usernamesave = 'Username : ' + username + '\n' 
    passwordsave = 'Password : ' + password + '\n'
    websave = 'Web Adress : ' + web + '\n'

    file.write(usernamesave)
    file.write(passwordsave)
    file.write(websave)
    file.close
    encrypt

def clearfile(): #need to be able to only clear some things, will do that later
    open('passwordmanager.txt', 'w').close
    encrypt

def readfile():
    file = open('passwordmanager.txt', 'r')
    content = file.read()
    file.close
    print(content)
    encrypt

def encrypt():
    file = open('passwordmanager.txt', 'r').read()
    base64.b64encode(file)
    file.close

def decrypt():
    file = open('passwordmanager.txt', 'r').read()
    base64.b64decode(file)
    file.close

#plug in commands to see what they do, keep textfilecheck 
textfilecheck()
