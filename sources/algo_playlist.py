import requests
import json
import random
from sources.math.file import *
from sources.math.pile import *


def creer_playlist(genre_prefere: str, artistes: Pile, age_utilisateur: int):
    """
    Creer une playlist de 20 musiques en utilisant l'API de Deezer
    
    Arguments:
    - genre_prefere (str): Le genre musical préféré de l'utilisateur
    - artistes_favoris (list): Liste de 3 noms d'artistes favoris
    - age_utilisateur (int): Âge de l'utilisateur (ex : 20)
    
    Retourne:
    - list: Une playlist contenant 15 musiques (titre + artiste + id)
    """
    artistes_favoris = []
    for _ in range(artistes.taille()):
        artistes_favoris.append(artistes.depiler())

    # URL de base de l'API Deezer
    base_url = "https://api.deezer.com/search?q="

    # Liste pour stocker les musiques
    playlist = []

    # Récupérer des musiques selon le genre préféré
    genre_url = base_url + genre_prefere
    reponse_genre = requests.get(genre_url)
    tabJSON_genre = json.loads(reponse_genre.text)
    var1 = random.randint(2, 4)
    var2 = random.randint(3, 4)
    var3 = random.randint(5, 6)
    for objet in tabJSON_genre["data"][:var1]:  # permet d aller chercher des musiques differentes
        musique = {
            "artist": objet["artist"]["name"],
            "titre": objet["title"],
            "id_son": objet["id"],
            "cover": objet["artist"]["picture_medium"]
        }
        playlist.append(musique)

    # Récupérer des musiques pour chaque artiste favori
    for artiste in artistes_favoris:
        artiste_url = base_url + artiste
        reponse_artiste = requests.get(artiste_url)
        tabJSON_artiste = json.loads(reponse_artiste.text)

        for objet in tabJSON_artiste["data"][:var2]:  # permet d aller chercher des musiques differentes
            musique = {
                "artist": objet["artist"]["name"],
                "titre": objet["title"],
                "id_son": objet["id"],
                "cover": objet["artist"]["picture_medium"]
            }
            playlist.append(musique)
    # Ajouter quelques musiques "en désaccord" avec l'âge de l'utilisateur
    if age_utilisateur < 20:
        recherche = "classique années 60"
    elif 20 <= age_utilisateur <= 40:
        recherche = "classique+médiéval"
    elif 40 < age_utilisateur <= 60:
        recherche = "electro moderne"
    else:
        recherche = "rap moderne+techno"

    # Récupérer des musiques correspondant au désaccord
    desaccord_url = base_url + recherche
    reponse_desaccord = requests.get(desaccord_url)
    tabJSON_desaccord = json.loads(reponse_desaccord.text)

    for objet in tabJSON_desaccord["data"][:var3]:
        musique = {
            "artist": objet["artist"]["name"],
            "titre": objet["title"],
            "id_son": objet["id"],
            "cover": objet["artist"]["picture_medium"]
        }
        playlist.append(musique)

    # Limiter la playlist à 20 musiques
    playlist = playlist[:20]

    f = File()
    for elt in playlist:
        f.enfiler(elt)
    return f


if __name__ == "__main__":
    age_utilisateur = 25
    genre = "rap"
    artistes_favoris = Pile()
    artistes_favoris.empiler("mac miller")
    artistes_favoris.empiler("sch")
    artistes_favoris.empiler("alpha wann")
    playlist = creer_playlist(genre, artistes_favoris, age_utilisateur)
    print(playlist)
