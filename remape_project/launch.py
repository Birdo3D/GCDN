from os import *
import app_data as app
import user_data as data
from remape_project.user_data import get_registered_user


def __first_start():
    try:
        mkdir('playlists')
        data.make_file()
        app.create_data()
    except:
        print("Le dossier n'a pas pu être créé.")


def start():
    if not path.exists("playlists"):
        __first_start()
    else:
        try:
            app.log()
            for id in data.get_registered_ids():
                data.add_user(get_registered_user(id))
        except:
            print("Le fichier n'a pas pu être ouvert.")
