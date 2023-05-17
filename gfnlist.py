import wget
import json
import os
import sys
import requests
from privkey import key
import csv

header = "\
  ___________________                           _______                  \n\
 /  _____/\_   _____/__________   ____  ____    \      \   ______  _  __ \n\
/   \  ___ |    __)/  _ \_  __ \_/ ___\/ __ \   /   |   \ /  _ \ \/ \/ / \n\
\    \_\  \|     \(  <_> )  | \/\  \__\  ___/  /    |    (  <_> )     /  \n\
 \______  /\___  / \____/|__|    \___  >___  > \____|__  /\____/ \/\_/   \n\
        \/     \/                    \/    \/          \/                \n"

def main():

    menu()

def menu():

    print (header)
    print ("version 0.1")

    choice = input("""
                      A: DOWNLOAD
                      Q: Quit/Log Out
                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        download()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select a function like A or Q.")
        print("Please try again")
        menu()

def download() :
    if not os.path.exists('gfnpc.json') :
        fs = wget.download(url='https://static.nvidiagrid.net/supported-public-game-list/locales/gfnpc-en-US.json', out='gfnpc.json')

if __name__ == '__main__':
    main()