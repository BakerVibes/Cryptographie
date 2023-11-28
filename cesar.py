def cryptage(chaine: str, decalage: int) -> str:    
    message = ""
    for i in chaine:
        if i.isalpha():
            if i.isupper():  # Si la lettre est en majuscule
                # Appliquer le décalage à la lettre majuscule
                message += chr(((ord(i) - 65) + decalage) % 26 + 65)
            elif i.islower(): # Si la lettre est en minuscule
                # Appliquer le décalage à la lettre minuscule
                message += chr(((ord(i) - 97) + decalage) % 26 + 97)
        else:
            message += i  # Conserver les caractères non alphabétiques
    return message

def decryptage(chaine: str, decalage: int) -> str:    
    message = ""
    for i in chaine:
        if i.isalpha():
            if i.isupper():  # Si la lettre est en majuscule
                # Appliquer le décalage inverse à la lettre majuscule
                message += chr(((ord(i) - 65) - decalage) % 26 + 65)
            elif i.islower(): # Si la lettre est en minuscule
                # Appliquer le décalage inverse à la lettre minuscule
                message += chr(((ord(i) - 97) - decalage) % 26 + 97)
        else:
            message += i  # Conserver les caractères non alphabétiques
    return message

choix = int(input("Tapez 1 pour chiffrer et 2 pour déchiffrer : "))
if choix == 1:
    chaine = input("Entrez une chaîne de caractères à crypter : ")
    decalage = int(input("Entrez la valeur du décalage : "))
    print("Message chiffré : ", cryptage(chaine, decalage))
elif choix == 2:
    chaine = input("Entrez une chaîne de caractères à déchiffrer : ")
    decalage = int(input("Entrez la valeur du décalage : "))
    print("Message déchiffré : ", decryptage(chaine, decalage))
else:
    print("Choix incorrect.")
