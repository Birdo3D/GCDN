class User:
    def __init__(self, id: int, name: str, mdp: str, age: int, genre: str, artists):
        """Création d'un nouvel utilisateur"""
        self.__id = id
        self.__name = name
        self.__mdp = mdp
        self.__age = age
        self.__genre = genre
        self.__artists = artists

    def set_mdp(self, mdp: str):
        """Met à jour le mot de passe de l'utilisateur"""
        self.__mdp = mdp

    def get_mdp(self):
        return self.__mdp

    def is_mdp(self, mdp: str) -> bool:
        """Test si le mot de passe correspond à celui de l'utilisateur"""
        return self.__mdp == mdp

    def set_name(self, name: str):
        """Met à jour le pseudonyme de l'utilisateur"""
        self.__name = name

    def get_name(self) -> str:
        """Renvoie le pseudonyme de l'utilisateur"""
        return self.__name

    def get_id(self) -> int:
        """Renvoie l'identifiant de l'utilisateur"""
        return self.__id

    def set_age(self, age: int):
        """Met à jour l'âge de l'utilisateur"""
        self.__age = age

    def get_age(self) -> int:
        """Retourne l'âge de l'utilisateur"""
        return self.__age

    def get_genre(self) -> str:
        """Retourne le genre préféré de l'utilisateur"""
        return self.__genre

    def set_genre(self, genre: str):
        """Met à jour le genre préféré de l'utilisateur"""
        self.__genre = genre

    def get_artists(self):
        """Retourne les artistes préférés de l'utilisateur"""
        return self.__artists

    def set_artists(self, artists):
        """Met à jour les artistes préférés de l'utilisateur"""
        self.__artists = artists
