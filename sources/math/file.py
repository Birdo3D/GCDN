class File:
    def __init__(self):
        """Création d'une file vide"""
        self.__file = []

    def enfiler(self, x):
        """Ajoute l'élément x à la queue de la file"""
        self.__file.append(x)

    def defiler(self):
        """Retire et retourne l'élément en tête de la file"""
        if len(self.__file) > 0:
            t = self.__file.pop(0)
            return t
        return None

    def file_vide(self) -> bool:
        """Retourne True si la file est vide et False dans le cas contraire"""
        return len(self.__file) == 0

    def longueur(self) -> int:
        """Retourne la longueur de file"""
        return len(self.__file)

    def tete(self):
        """Retourne l'élément en tête de la file"""
        return self.__file[0]

    def queue(self):
        """Retourne l'élément à la queue de la file"""
        return self.__file[len(self.__file) - 1]

    def copy(self):
        """Retourne une copie de la file"""
        new_file = File()
        new_file.__file = self.__file[:]
        return new_file

    def __str__(self):
        """Affichage de la file"""
        if self.file_vide():
            return "None"
        res = "--> "
        for i in range(len(self.__file)):
            res += str(self.__file[i])
            if i != len(self.__file) - 1:
                res += " | "
            else:
                res += " -->"
        return res

    def __add__(self, other):
        """Concaténation de files"""
        return self.__file + other.__file


if __name__ == '__main__':
    f = File()
    print("Nouvelle file :", f)
    f.enfiler(12)
    print("Enfiler 12... Etat de la file :", f)
    print("La file est vide ? :", f.file_vide())
    print("Taille de la file :", f.longueur())
    f.enfiler(5)
    print("Enfiler 5... Etat de la file :", f)
    print("Tête de file :", f.tete())
    print("Queue de file :", f.queue())
    print("Défiler :", f.defiler())
    print("Etat de la file :", f)
    print("Défiler :", f.defiler())
    print("Etat de la file :", f)
    print("La file est vide ? :", f.file_vide())
