__alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", " ", ".", "'", "!", "?"]


def __chiffrement_affine(a: int, b: int, s: str) -> str:
    """
        Le procédé de chiffrement d'une lettre s'effectue de la manière suivante :
        -Etape 1 : on choisit une clé de codage constituée de deux nombres a et b, avec a non nul.
        -Etape 2 : à chaque symbole s qu'on veut coder, on associe un nombre x correspondant à l'indice du symbole dans la liste "alphabet" décrite plus haut.
        -Etape 3 : on calcule le reste y de a*m+b par la division euclidienne par 31.
        -Etape 4 : au nombre y, on associe le symbole z correspondant dans la liste de départ.

        Remarque :
        Le chiffrement affine est un codage par substitution. Chaque caractère est codé par un unique autre caractère dans la liste "alphabet".
    """
    x = __alphabet.index(s)
    y = (a * x + b) % 31
    c = __alphabet[y]
    return c


def chiffrement_message(a: int, b: int, m: str) -> str:
    """
        Encode une chaîne de caractères à l'aide du chiffrement affine.
        :param a: Entier naturel non nul
        :param b: Entier naturel
        :param m: Message à encoder
        :return: Message encodé
    """
    c = ""
    for char in m:
        c = c + __chiffrement_affine(a, b, char.upper())
    return c


def chiffrement_vigenere(key: str, text: str) -> str:
    """
        Encore une chaîne de caractères à l'aide du chiffrement de Vigenère.
        :param key: Clé d'encodage
        :param text: Message à encoder
        :return: Message encodé
    """
    texte_chiffre = ""
    for lettre in text:
        texte_chiffre = texte_chiffre + str(__alphabet.index(lettre.upper()))
    texte_cle = ""
    for char in key:
        texte_cle = texte_cle + str(__alphabet.index(char.upper()))
    z_chaine = ""
    j = 0
    for i in range(len(text)):
        if j >= len(texte_cle):
            j = 0
        z_chaine = z_chaine + str(int(texte_chiffre[i]) + int(texte_cle[j]))
        j = j + 1
    result = ""
    for chiffre in z_chaine:
        result = result + __alphabet[int(chiffre)]
    return result


if __name__ == '__main__':
    print(chiffrement_vigenere("test", "Lycee"))
