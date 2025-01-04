from time import gmtime, strftime
from xml.etree.ElementTree import *

__path = "save.xml"


def create_data():
    """Création du fichier save.xml"""
    root = Element("app")
    second = SubElement(root, "info")
    SubElement(second, "users-count").text = "0"
    SubElement(second, "start-count").text = "1"
    first = SubElement(second, "first-start")
    SubElement(first, "date").text = str(strftime("%d/%m/%Y"))
    SubElement(first, "time").text = str(strftime("%H:%M:%S", gmtime()))
    last = SubElement(second, "last-start")
    SubElement(last, "date").text = str(strftime("%d/%m/%Y"))
    SubElement(last, "time").text = str(strftime("%H:%M:%S", gmtime()))
    tree = ElementTree(root)
    indent(tree, space="    ")
    tree.write(__path)

def log():
    """Log le nouveau démarrage de l'application"""
    tree = parse(__path)
    root = tree.getroot()
    root[0][1].text = str(int(root[0][1].text) + 1) # Increment start counter
    root[0][3][0].text = str(strftime("%d/%m/%Y")) # Change last start date
    root[0][3][1].text = str(strftime("%H:%M:%S", gmtime())) # Change last start time
    tree.write(__path)


def get_ids():
    """Retourne le nombre total d'utilisateurs enregistrés"""
    try:
        tree = parse(__path)
        root = tree.getroot()
        return int(root[0][0].text)
    except:
        pass


def inc_ids():
    """Incrémente le nombre total d'utilisateurs enregistrés"""
    try:
        tree = parse(__path)
        root = tree.getroot()
        root[0][0].text = str(int(root[0][0].text) + 1)
        tree.write(__path)
        return 1
    except:
        return -1

def generate_id() -> int:
    """Generate an id for a new user"""
    return int(get_ids()) + 1
