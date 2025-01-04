from os import *
import app_data as data


def __first_start():
    try:
        mkdir('user_data')
        mkdir('playlists')
        mkdir('app_data')
        data.create_data()
    except:
        print("Le dossier n'a pas pu être créé.")


def start():
    if not path.exists("app_data"):
        print("hello world !")
        __first_start()
    else:
        try:
            data.log()
            for file in listdir('user_data'):
                print("fichier", file)
                # print("fichier", find_data(file))
        except:
            print("Le fichier n'a pas pu être ouvert.")
