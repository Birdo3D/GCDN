import json
from remape_project.sources.user_data import *

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
