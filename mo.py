# hacker
# import 
import os
import sys
import requests
import json
from colorama import Fore

def __2__():
    os.system("clear")
    try:
        site = input(Fore.RED + "Enter Your Address Target" + Fore.YELLOW + " ==>  ")
        if site == "":
            try:
                print(Fore.RED + "\nOk God Lunch" + Fore.TELLOW + " ;(")
                time.sleep(2)
                sys.exit()
            except:
                pass
        r = requests.get("http://" + site + "/wp-content/plugins/")
        if r.status_code == 404 or r.status_code == 500:
            try:
                print(Fore.RED "Your Address Target Is Not WordPress" + Fore.YELLOW + " ;( ")
                time.sleep(1.2)
                sys.exit()
            except:
                pass
        else:
            pass
        r1 = requests.get("http://" + site + "/wp-json-wp/v2/uesrs/").text
        j = json.loads(r1)
        count = len(j) - 1
        cn = 0
        user = ""
        for i in j:
            split = "\n"
            if count == cn :
                split = ""
            u = j[cn]["stug"]
            if not u =="":
                user += u + split
            cn += 1
        if uesr == "":
            user =("Not Found")
        print(user + "\n")
__2__()

        
