import sources.app_data as app
from xml.etree.ElementTree import *
from sources.math.pile import Pile
from sources.user import *
from sources.math.encrypter import *

__users = []
__main_user = None
__path = "../data/users.xml"


def create_user(name: str, mdp: str, age: int, genre: str, artists) -> bool:
    """Ajoute un utilisateur à l'application"""
    id = app.generate_id()
    user = User(id, name, chiffrement_mystere(get_char(int(str(id)[0])), mdp), age, genre,
                artists)  # Create user object & Encrypt password
    if not __user_registered(user):
        app.inc_ids()  # Increment user count
        add_user(user)  # Register user in app
        set_default_user(user)  # Set default user in app
        __register_user(user)  # Register user in users.xml
        return True  # Tout s'est correctement dérouler dans la création du nouvel utilisateur
    else:
        return False  # Ce nom est déjà pris


def add_user(user):
    __users.append(user)


def get_users():
    return __users.copy()


def set_default_user(user):
    global __main_user
    __main_user = user


def get_default_user():
    return __main_user


def __register_user(user):
    root = Element("users")
    second = SubElement(root, "user", attrib={"id": str(user.get_id())})
    SubElement(second, "name").text = user.get_name()
    SubElement(second, "password").text = str(user.get_mdp())
    SubElement(second, "age").text = str(user.get_age())
    SubElement(second, "genre").text = str(user.get_genre())
    titles = SubElement(second, "artists")
    arts = user.get_artists().copy()
    for i in range(arts.taille()):
        SubElement(titles, "artist-id").text = arts.depiler()
    tree = ElementTree(root)
    indent(tree, space="    ")
    tree.write(__path)


def make_file():
    root = Element("users")
    """second = SubElement(root, "user", attrib={"id": "0"})
    SubElement(second, "name").text = "nametest"
    SubElement(second, "age").text = "25"
    """
    tree = ElementTree(root)
    indent(tree, space="    ")
    tree.write(__path)


def get_registered_user(id: int):
    tree = parse(__path)
    for elt in tree.getroot():
        if int(elt.attrib["id"]) == id:
            arts = Pile()
            for m in elt[4]:
                arts.empiler(m.text)
            return User(int(elt.attrib["id"]), elt[0].text, elt[1].text, int(elt[2].text), elt[3].text, arts)


def get_registered_ids():
    ids = []
    tree = parse(__path)
    for elt in tree.getroot():
        ids.append(int(elt.attrib["id"]))
    return ids


def __user_registered(user) -> bool:
    """Retourne si un utilisateur avec le même nom existe déjà dans la base de donnés"""
    tree = parse(__path)
    for elt in tree.getroot():
        return str(user.get_name()) == elt[0].text


def user_exist(name: str) -> bool:
    for user in __users:
        return user.get_name() == name
    return False

def get_user(name: str) -> User:
    for user in __users:
        if user.get_name() == name:
            return user

def update_user(user: User, name: str, age: int, genre: str, artists: Pile, pwd: str):
    tree = parse(__path)
    main = ""
    for elt in tree.getroot():
        if int(elt.attrib["id"]) == user.get_id():
            main = elt
    if name is not None:
        user.set_name(name)
        main[0].text = name
    if age is not None:
        user.set_age(age)
        main[2].text = str(age)
    if genre is not None:
        user.set_genre(genre)
        main[3].text = genre
    if artists is not None:
        user.set_artists(artists)
        for i in range(artists.taille()):
            main[4][i].text = artists.depiler()
    if pwd is not None:
        user.set_mdp(pwd)
        main[1].text = pwd
    tree.write(__path)
