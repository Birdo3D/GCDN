from user import *
import app_data as app
from xml.etree.ElementTree import *
from encrypter import *

__users = []
__main_user = None
__path = "users.xml"


def create_user(name: str, mdp: str, age: int, musics: list) -> bool:
    """Ajoute un utilisateur à l'application"""
    id = app.generate_id()
    user = User(id, name, chiffrement_vigenere(get_char(int(str(id)[0])), mdp), age, musics) # Create user object & Encrypt password
    if not __user_registered(user):
        app.inc_ids() # Increment user count
        add_user(user) # Register user in app
        set_default_user(user) # Set default user in app
        __register_user(user) # Register user in users.xml
        return True # Tout s'est correctement dérouler dans la création du nouvel utilisateur
    else:
        return False # Ce nom est déjà pris


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
    titles = SubElement(second, "musics")
    for music in user.get_musics():
        SubElement(titles, "title-id").text = "4568"
    tree = ElementTree(root)
    indent(tree, space="    ")
    tree.write(__path)


def make_file():
    root = Element("users")
    second = SubElement(root, "user", attrib={"id": "0"})
    SubElement(second, "name").text = "nametest"
    SubElement(second, "age").text = "25"
    tree = ElementTree(root)
    indent(tree, space="    ")
    tree.write(__path)

def get_registered_user(id: int):
    tree = parse(__path)
    for elt in tree.getroot():
        if int(elt.attrib["id"]) == id:
            titles = []
            for m in elt[3]:
                titles.append(m.text)
            return User(int(elt.attrib["id"]), elt[0].text, elt[1].text, int(elt[2].text), titles)

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
