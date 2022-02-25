#função recebe caractere e devolve True se for vogal e False se for consoante

vogais = ("a", "e", "i", "o", "u")
vogais_maiusculas = ("A", "E", "I","O","U")

def vogal (x):
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U"):
        return True
    else:
        return False

