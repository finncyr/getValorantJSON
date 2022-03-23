import requests
import PySimpleGUI as sg
import datetime
import json
from dotenv import load_dotenv
from os import getenv

load_dotenv()
headers = { "X-Riot-Token": getenv('RIOT_API_KEY') }

baseicon = b'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'

sg.theme('Dark Blue 3')

layout = [[sg.Text('Playername:')],
          [sg.Input('', enable_events=True,  key='-input-name-')],
          [sg.Text('Tag:')],
          [sg.Input('', enable_events=True,  key='-input-tag-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Update latest match', key='-update-'), sg.Button('Exit')]]

window = sg.Window('getValorantJSON', layout, icon=baseicon)

def get_score(player):
    return player['stats']['score']

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == '-update-':
        url = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + values['-input-name-'] + '/' + values['-input-tag-'] + '/'
        response = requests.request("GET", url, headers=headers)
        j = response.json()
        url = "https://eu.api.riotgames.com/val/match/v1/matchlists/by-puuid/" + j['puuid']
        response = requests.request("GET", url, headers=headers)
        j = response.json()
        matchid = j['history'][0]['matchId']
        lastgametime = datetime.datetime.fromtimestamp( (j['history'][0]['gameStartTimeMillis']) // 1000)
        window['-OUTPUT-'].update("Current Match: " + lastgametime.strftime("%d.%m.%Y, %H:%M:%S"))
        url = "https://eu.api.riotgames.com/val/match/v1/matches/" + matchid
        response = requests.request("GET", url, headers=headers)
        j = response.json()

        with open('json_response.json', 'w') as outfile:
            json.dump(j, outfile)

        playerobj = {"playersRed": [], "playersBlue": []}

        print(playerobj)

        for player in j['players']:
            if player['teamId'] == "Blue":
                playerobj['playersBlue'].append(player)
            if player['teamId'] == "Red":
                playerobj['playersRed'].append(player)
        
        playerobj['playersBlue'].sort(reverse=True, key=get_score);
        playerobj['playersRed'].sort(reverse=True, key=get_score);

        with open('sortedplayers.json', 'w') as outfile2:
            json.dump(playerobj, outfile2)

# Finish up by removing from the screen
window.close()