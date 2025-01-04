from user import *
from os import *
import app_data as data
from xml.etree.ElementTree import *

users = []
main_user = ""


def __get_path(user):
    return "app_data\\" + str(user.get_id) + ".xml"


def create_user(name, age, mdp, musics):
    user = User(name, mdp, age, musics)
    if not user_registered(user):
        register_user(user)


def register_user(user):
    users.append(user)


def user_exist(user) -> bool:
    return user in users


def set_default_user(user):
    user_main = user


def get_user(name: str):
    for user in users:
        if user.get_name() == name:
            return user


def get_user(id: int):
    for user in users:
        if user.get_id() == id:
            return user


def create_data(user):
    root = Element("user")
    SubElement(root, "id").text = str(user.get_id())
    SubElement(root, "name").text = user.get_name()
    SubElement(root, "age").text = str(user.get_age())
    tree = ElementTree(root)
    tree.write(__get_path(user))


def find_data(file):
    tree = parse(file)
    root = tree.getroot()
    return int(root[0].text), root[1].text, int(root[2].text)


def user_registered(user):
    try:
        for file in listdir('user_data'):
            if user.get_id() == file[:-5]:
                return True
        return False
    except:
        print("Le fichier n'a pas pu être ouvert.")


def generate_id() -> int:
    """Generate an id for a new user"""
    data.inc_ids()
    return int(data.get_ids()) + 1
