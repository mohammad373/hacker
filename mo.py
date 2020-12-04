# hacker
import socket
import sys
import time
from colorama import Fore

while True:
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
            try:
                print(Fore.GREEN + "Pleass Enter For Go To The Mano :)")
                i = input("")
                if i == "":
                    try:
                        print(Fore.RED + "You Are 5 Sec Go To The Mano ;)")
                        time.sleep(5)
                        sys.exit()
                    except:
                        pass
                if i !="":
                    try:
                        print(Fore.RED + "Not Found ;)")
                        time.sleep()
                        sys.exit()
                    except:
                        pass
            except:
                pass
    __name__()
