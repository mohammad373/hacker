# hacker
import socket
import sys
import time
from colorama import Fore
def __name__():
        try:
            print(Fore.GREEN + "\n\nHello . Welcome Back ;)\n")
            time.sleep(3)
            site = input(Fore.BLUE + "Enter Your Address WebSite ==> ")
            if site == "":
                try:
                    print(Fore.GREEN + "You Are 5 Sec Go To The Mano ;)")
                    time.sleep(5)
                    sys.exit()
                except:
                    pass
            my_socket = socket.gethostbyname(str(site))
            print(Fore.GREEN + "Ip Web Site ==> "+ Fore.RED + my_socket)

        except:
                pass
    __name__()
