import socket
import os
import privateserver
import random
from slowprint import slowprint
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
from os import system
import ctypes
import time

# VERSION REPORTING
# REMEMBER TO CHANGE THIS
ver = 1.0



def err(type, msg):
    print("We encountered an error. Here are the details:")
    print("Type:", type, "Message", msg)
s = socket.socket()
st = 0.02
def sp(text):
  for char in text:
    print(Fore.LIGHTGREEN_EX + char, end="", flush=True)
    time.sleep(st)
ctypes.windll.kernel32.SetConsoleTitleW("NOCOM")
# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose a random color for the client
client_color = random.choice(colors)
sp("Initializing...")
print("")
time.sleep(1)
sp("Locating data...")
print("")
time.sleep(1)
sp("Found module NETWORK_EXPL:NOCOM.")
print("")
time.sleep(1)
sp("Loaded NOCOM from NETWORK_EXPL")
print("")
time.sleep(1)
ctypes.windll.kernel32.SetConsoleTitleW("PyNet Version 1.1")
def pubchat():
    # server's IP address
    # if the server is not on this machine, 
    # put the private (network) IP address (e.g 192.168.1.2)
    sp("Enter IP to connect to:")
    SERVER_HOST= input ("")
    SERVER_PORT = 5002 # server's port
    separator_token = "<SEP>" # we will use this to separate the client name & message
    sp("Hooking into network thread...")
    time.sleep(1)
    print("")

    # initialize TCP socket
    sp(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    print("")
    # connect to the server
    sp("Hooked.")
    print("")
    s.connect((SERVER_HOST, SERVER_PORT))
    sp("[+] Connected.")
    print("")
    # prompt the client for a name
    name = input("Enter your name: ")

    sp("You can start chatting. Type q to return to the menu.")
    print("")
    def listen_for_messages():
        while True:
            message = s.recv(1024).decode()
            print("\n" + message)
    # make a thread that listens for messages to this client & print them
    t = Thread(target=listen_for_messages)
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
    while True:
        # input message we want to send to the server
        to_send =  input(">")
        # a way to exit the program
        if to_send.lower() == 'q':
            break
        # add the datetime, name & the color of the sender
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
        # finally, send the message
        s.send(to_send.encode())
    choice()
def privchat():
    print("Do you want to host or connect to a private server?")
    print("""
    (1) Host
    (2) Connect

    """)
    privchoice = input(">")
    if privchoice == "1":
        privcode = random.randint(1025, 65536)
        print(">", privcode, "< This is your private server code. This changes every time you host, so keep that in mind")
        tempprivip = socket.gethostname() 
        privip = socket.gethostbyname(tempprivip)
        print(">", privip, "< This is your IP. It does not change every time you host.")
        print("You will have to give both of these to the people who are connectiing to you.")
        print("Initializing server...")
        privateserver.run(privcode)
    if privchoice == "2":
            # server's IP address
        # if the server is not on this machine, 
        # put the private (network) IP address (e.g 192.168.1.2)
        print("Enter IP to connect to:")
        SERVER_HOST= input (">")
        print("Enter your private server code:")
        SERVER_PORT = input (">")
        SERVER_PORT = int(SERVER_PORT)
        separator_token = "<SEP>" # we will use this to separate the client name & message
        sp("Hooking into network thread...")
        time.sleep(1)
        print("")

        # initialize TCP socket
        sp(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        print("")
        # connect to the server
        sp("Hooked.")
        print("")
        s.connect((SERVER_HOST, SERVER_PORT))
        sp("[+] Connected.")
        print("")
        # prompt the client for a name
        name = input("Enter your name: ")

        sp("You can start chatting. Type q to return to the menu.")
        print("")
        def listen_for_messages():
            while True:
                message = s.recv(1024).decode()
                print("\n" + message)
        # make a thread that listens for messages to this client & print them
        t = Thread(target=listen_for_messages)
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()
        while True:
            # input message we want to send to the server
            to_send =  input(">")
            # a way to exit the program
            if to_send.lower() == 'q':
                break
            # add the datetime, name & the color of the sender
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
            # finally, send the message
            s.send(to_send.encode())
        choice()

def gamemenu():
    print("This is still in progress, crap may just ramdomly crash your computer if it feels like it")
    print("""
    (1) Host a Doom server
    (2) Connect to a Doom server
    (3) Snake?
    (4) Back
    """)
    gamechoice = input("Enter your choice>")
    if gamechoice == "1":
        err("02", "Not implemented")
        gamemenu()
    if gamechoice == "2":
        err("02", "Not implemented")
        gamemenu()
    if gamechoice == "3":
        os.startfile("notsnake.py")
        gamemenu()
    if gamechoice == "4":
        choice()
def choice():
    os.system('cls')
    print("""
Welcome to PyNet! This is a local messaging service, sorta like a BBS.

What would you like to do?
(1) Public chat [IN DEVELOPMENT]
(2) Join or Create a Private Chat    
(3) Games          
(4) About

    """)
    boardchoice = input("Enter your choice>")
    if boardchoice == "1":
        print("Why would you choose this? Literaly nothing here.")

        choice()
    if boardchoice == "2":
        privchat()
    if boardchoice == "3":
        gamemenu()
    if boardchoice == "4":
        print("PyNet Version", ver)
        print("Developed by Xavier Hale")
        print("Version complied on 2/16/2023")
        choice()
choice()

    # close the socket
s.close()