import math

def cryptage(chaine: str, a: int, b: int) -> str:
    # Faire le cryptage    
    message = ''
    for i in chaine:
        if i.isalpha():
            if i.isupper():
                # Appliquer la formule de chiffrement affine pour les lettres majuscules
                lettre = chr(((a * (ord(i) - 65) + b) % 26) + 65)
            elif i.islower():
                # Appliquer la formule de chiffrement affine pour les lettres minuscules
                lettre = chr(((a * (ord(i) - 97) + b) % 26) + 97)
        else:
            lettre = i
        message += lettre            
    return message
    
def decryptage(chaine: str, a: int, b: int) -> str:
    # Faire le décryptage
    a_inv = pow(a, -1, 26)  # Calcul de l'inverse modulaire de a modulo 26

    message = ''
    for i in chaine:
        if i.isalpha():
            if i.isupper():
                # Appliquer la formule de déchiffrement affine pour les lettres majuscules
                lettre = chr(((a_inv * (ord(i) - 65 - b)) % 26) + 65)
            elif i.islower():
                # Appliquer la formule de déchiffrement affine pour les lettres minuscules
                lettre = chr(((a_inv * (ord(i) - 97 - b)) % 26) + 97)
        else:
            lettre = i
        message += lettre
    return message

choix = int(input("Tapez 1 pour crypter et 2 pour décrypter : "))
a = int(input("Entrez la valeur du paramètre a (il doit être premier avec 26): "))

# Vérifier si a et 26 sont premiers entre eux
pgcd = math.gcd(a, 26)
if pgcd == 1: # a et 26 sont premiers entre eux    
    b = int(input("Entrez la valeur du paramètre b : "))    
    if choix == 1:
        chaine = input("Entrez le texte que vous voulez crypter : ")
        print("Message crypté : ", cryptage(chaine, a, b))
    elif choix == 2:
        chaine = input("Entrez le texte que vous voulez décrypter : ")
        print("Message décrypté : ", decryptage(chaine, a, b))
    else:
        print("Choix erroné!!!")
else: # a et 26 ne sont pas premiers entre eux
    print("Le nombre ", a, " n'est pas premier avec 26.")
