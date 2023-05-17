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
                      A: Generate GFN STEAM LIST
                      B: Generate GFN STEAM CSV
                      Q: Quit/Log Out
                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        steamlist()
    if choice == "B" or choice =="b":
        gfnsteamcsv()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select a function like A or Q.")
        print("Please try again")
        menu()

def steamlist():
    with open('gfnpc.json', encoding="utf8") as f :
            games = json.loads(f.read())
            data = {}
            data['data'] = []
            for game in games :
                if game['steamUrl'] != '' :
                    sl = game['steamUrl']
                    data['data'].append({
                        'title': game['title'],
                        'id': sl.replace('https://store.steampowered.com/app/','')
                    })
            with open('steamlist.json', 'w') as outfile:
                json.dump(data, outfile)

def gfnsteamcsv():
    with open('steamlist.json', encoding="utf8") as f :
            d = json.loads(f.read())
            games = d['data']
            header = ['id', 'name', 'age', 'free', 'recommendations', 'date']
            datascience = []
            total = len(games)
            count = 0 
            with open('gfnsteam-temp.csv', 'w', newline ='', encoding='utf8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)
                for game in games :
                    g = requests.get("http://store.steampowered.com/api/appdetails/?appids="+game['id']+"&key="+key)
                    gamejson = g.json()
                    if gamejson != 'null' : 
                        if 'data' in gamejson[game['id']] : 
                            if 'recommendations' in gamejson[game['id']]['data'] :
                                print(gamejson[game['id']]['data']['name'] + ':' + str(gamejson[game['id']]['data']['steam_appid']))
                                print(str(count) + ' / ' + str(total))
                                datascience = [
                                    gamejson[game['id']]['data']['steam_appid'],
                                    gamejson[game['id']]['data']['name'],
                                    gamejson[game['id']]['data']['required_age'],
                                    gamejson[game['id']]['data']['is_free'],
                                    gamejson[game['id']]['data']['recommendations']['total'],
                                    gamejson[game['id']]['data']['release_date']['date']
                                ]
                                writer.writerow(datascience)
                                count = count + 1

#def gfnepiccsv():
    # TODO

#def gfnuplaycsv():
    # TODO

if __name__ == '__main__':
    main()
