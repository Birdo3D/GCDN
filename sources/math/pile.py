class Pile:
    def __init__(self):
        """Création d'une pile vide"""
        self.__pile = []

    def empiler(self, x):
        """Ajoute l'élément x au sommet de la pile"""
        self.__pile.append(x)

    def depiler(self):
        """Retire et retourne l'élément au sommet de la pile"""
        if len(self.__pile) > 0:
            t = self.__pile.pop()
            return t
        return None

    def pile_vide(self) -> bool:
        """Retourne True si la pile est vide et False dans le cas contraire"""
        return len(self.__pile) == 0

    def taille(self) -> int:
        """Retourne la taille de pile"""
        return len(self.__pile)

    def sommet(self):
        """Retourne l'élément au sommet de la pile"""
        if self.pile_vide() == False:
            return self.__pile[len(self.__pile) - 1]
        return None

    def copy(self):
        """Retourne une copie de la pile"""
        new_pile = Pile()
        new_pile.__pile = self.__pile[:]
        return new_pile

    def __str__(self):
        """Retourne le contenu de la pile"""
        if self.pile_vide():
            return "None"
        res = "[ "
        for i in range(len(self.__pile)):
            res += str(self.__pile[i])
            if i != len(self.__pile) - 1:
                res += " | "
        return res

    def __add__(self, other):
        """Concaténation de piles"""
        return self.__pile + other.__pile


if __name__ == '__main__':
    p = Pile()
    print("Nouvelle pile :", p)
    p.empiler(12)
    print("Empiler 12... Etat de la pile :", p)
    p.empiler(52)
    print("Empiler 52... Etat de la pile :", p)
    p.empiler(86)
    print("Empiler 86... Etat de la pile :", p)
    print("La pile est vide ? :", p.pile_vide())
    print("Taille de la pile :", p.taille())
    print("Tete de la pile :", p.sommet())
    print("Dépiler :", p.depiler())
    print("Etat de la pile :", p)
    print("La pile est vide ? :", p.pile_vide())
