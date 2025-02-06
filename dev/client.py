import socket
import os
import privateserver
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
from os import system
import ctypes
import time

# VERSION REPORTING
# REMEMBER TO CHANGE THIS

ver = 1.3

machine_Name = os.environ['COMPUTERNAME']

def err(type, msg):
    print("We encountered an error. Here are the details:")
    print("Type:", type, "Message", msg)


s = socket.socket()
st = 0.02

def fileshare():
    print("This is an early feature, expect bugs.")

def sp(text):
    for char in text:
        print(Fore.LIGHTGREEN_EX + char, end="", flush=True)
        time.sleep(st)


# init colors
init()

# set the available colors
colors = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.MAGENTA,
    Fore.RED,
    Fore.WHITE,
    Fore.YELLOW,
]
ctypes.windll.kernel32.SetConsoleTitleW("PyNet Version "+ver)
def privchat():
    print("Do you want to host or connect to a private server?")
    print(
        """
    (1) Host
    (2) Connect

    """
    )
    privchoice = input(">")
    if privchoice == "1":
        privcode = random.randint(1025, 65536)
        print(
            ">",
            privcode,
            "< This is your private server code. This changes every time you host, so keep that in mind",
        )
        tempprivip = socket.gethostname()
        privip = socket.gethostbyname(tempprivip)
        print(">", privip, "< This is your IP. It does not change every time you host.")
        print(
            "You will have to give both of these to the people who are connectiing to you."
        )
        print("Initializing server...")
        privateserver.run(privcode)
    if privchoice == "2":
        print("Enter IP to connect to:")
        SERVER_HOST = input(">")
        print("Enter your private server code:")
        SERVER_PORT = input(">")
        SERVER_PORT = int(SERVER_PORT)
        separator_token = (
            "<SEP>"  
        )
        sp(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        print("")
        s.connect((SERVER_HOST, SERVER_PORT))
        sp("[+] Connected.")
        print("")
        name = input("Enter your name: ")
        client_color = colors[random]
        sp("You can start chatting. Type q to return to the menu.")
        print("")

        def listen_for_messages():
            while True:
                message = s.recv(1024).decode()
                print("\n" + message)

        t = Thread(target=listen_for_messages)
        t.daemon = True
        t.start()
        while True:
            to_send = input(">")
            if to_send.lower() == "q":
                break
            date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
            s.send(to_send.encode())
        choice(0)


def choice(nclr):
    if nclr != 1 :
        os.system("cls")
    print(
        """
Welcome to PyNet!

What would you like to do?
(1) Public chat [IN DEVELOPMENT]
(2) Join or Create a Private Chat            
(3) About

    """
    )
    boardchoice = input("Enter your choice>")
    if boardchoice == "1":
        print("Temporary, when a permanent host is found this will be populated.")
        choice(0)
    if boardchoice == "2":
        privchat()
    if boardchoice == "3":
        print("PyNet Version", ver)
        print("Developed by Xavier Hale")
        print("Version complied on 2/5/2025")
        choice(1)


choice(0)

s.close()
