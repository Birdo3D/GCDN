# Créé par Gaël

import json
import requests

def recherche_album_id(nom):
    var='https://api.deezer.com/search?q='+nom
    reponse =requests.get(var)
    tabJSON = json.loads(reponse.text)
    return tabJSON["data"][0]["album"]["id"]

"""*************************************"""

def recherche_genre_id(nom):
    id_album=recherche_album_id(nom)
    var='https://api.deezer.com/album/'+str(id_album)
    reponse =requests.get(var)
    tabJSON = json.loads(reponse.text)
    return tabJSON["genre_id"]

"""*************************************"""

def trouver_genre(nom):
    id_genre=recherche_genre_id(nom)
    var='https://api.deezer.com/genre'
    reponse =requests.get(var)
    tabJSON = json.loads(reponse.text)
    for objet in tabJSON['data']:
        try:
            if objet["id"]==id_genre:
                return objet["name"]
        except:
            pass
"""*************************************"""

dico= {
    "nom": "a",
    "genre": "b",
    "albums": [
    ]
}

def cover_album(id_album):
    var='https://api.deezer.com/album/'+str(id_album)
    reponse =requests.get(var)
    tabJSON = json.loads(reponse.text)
    return tabJSON["cover_medium"]

"""*************************************"""

def recherche_id_titre_son(id_album):
    var='https://api.deezer.com/album/'+str(id_album)
    reponse =requests.get(var)
    tabJSON = json.loads(reponse.text)
    liste_titres = []
    for objet in tabJSON["tracks"]["data"]:
        titre_son = {
            "id_son": objet["id"],
            "titre": objet["title"]
        }
        liste_titres.append(titre_son)
    return liste_titres
"""*************************************"""

def album_artiste(nom):
    liste_album=[]
    liste_album_trié=[]
    var='https://api.deezer.com/search?q='+nom
    reponse =requests.get(var)
    tabJSON = json.loads(reponse.text)
    for objet in tabJSON['data']:
        b=objet["album"]["id"]
        liste_album.append(b)
    for elt in liste_album:
        if elt not in liste_album_trié:
            liste_album_trié.append(elt)  
    return liste_album_trié

"""*************************************"""

def nom_album(id_album):
    var='https://api.deezer.com/album/'+str(id_album)
    reponse =requests.get(var)
    tabJSON = json.loads(reponse.text)
    return tabJSON["title"]

"""*************************************"""
def cree_album(nom):
    liste_album = album_artiste(nom)
    liste=[]
    for id_album in liste_album:
        album = {
            "id_album": id_album,
            "titre": nom_album(id_album),
            "cover": cover_album(id_album),
            "sons": recherche_id_titre_son(id_album)
        }
        liste.append(album)
    dico["albums"].append(liste)
    return dico

"""*************************************"""

def info_complet(nom):
    dico["nom"]=nom
    dico["genre"]=trouver_genre(nom)
    info_album=cree_album(nom)
    dico["albums"].append(info_album)
    return dico
nom = input("Veuillez entrer vos artistes du moment: ")
print(info_complet(str(nom)))
