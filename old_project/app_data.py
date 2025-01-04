from datetime import date
from xml.etree.ElementTree import *

path = ("app_data\\" + "save.xml")


def create_data():
    root = Element("app")
    second = SubElement(root, "info")
    SubElement(second, "users-count").text = "0"
    SubElement(second, "first-start").text = str(date.today().strftime("%d/%m/%Y"))
    SubElement(second, "last-start").text = str(date.today().strftime("%d/%m/%Y"))
    tree = ElementTree(root)
    tree.write(path)

def log():
    tree = parse(path)
    root = tree.getroot()
    root[0][2].text = str(date.today().strftime("%d/%m/%Y"))
    tree.write(path)


def get_ids():
    try:
        tree = parse(path)
        root = tree.getroot()
        return int(root[0][0].text)
    except:
        pass


def inc_ids():
    try:
        """dt = json.load(open(path, "r"))["users-number"] + 1
        json.dump({"users-number": dt}, open(path, "w"), indent=4)"""
        tree = parse(path)
        root = tree.getroot()
        root[0][0].text = str(int(root[0][0].text) + 1)
        tree.write(path)
        return 1
    except:
        return -1
