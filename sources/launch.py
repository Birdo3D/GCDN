from os import *
import sources.user_data as data
import sources.app_data as app


def __first_start():
    try:
        mkdir('../data/playlists')
        data.make_file()
        app.create_data()
    except:
        print("Le dossier n'a pas pu être créé.")


def start():
    if not path.exists("../data/playlists"):
        __first_start()
    else:
        try:
            app.log()
            for id in data.get_registered_ids():
                data.add_user(data.get_registered_user(id))
        except:
            print("Le fichier n'a pas pu être ouvert.")
