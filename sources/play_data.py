import json
from sources.user_data import *
import os
from sources.math.file import *

__path = "../data/playlists/"


def export_playlist(playlist, name: str):
    try:
        f = open(__path + name + ".json", 'w', encoding='utf-8')
        data = {'creator-id': get_default_user().get_id()}
        for i in range(playlist.longueur()):
            data["title" + str(i)] = playlist.defiler()
        json.dump(data, f, indent=4)
    except:
        print("La playlist n'a pas été exportée !")


def get_playlists():
    plays = []
    for play in os.listdir(__path):
        plays.append(play[:-5])
    return plays

def get_playlist(name):
    f = open(__path + name + ".json", 'r', encoding='utf-8')
    data = json.load(f)
    play = File()
    for elt in data.keys():
        if elt[:5] == "title":
            play.enfiler(data[elt])
    return play
