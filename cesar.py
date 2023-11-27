def cryptage (chaine: str, decalage: int)-> str:    
    message = ""
    for i in chaine:
        if i == ' ':
            message += i
        else :
            if i.isupper():  # Si la lettre est en minuscule
                message += chr(((ord(i) - 65 ) + decalage) % 26 + 65)
            elif i.islower(): # Si la lettre est en majuscule
                message += chr(((ord(i) - 97 ) + decalage) % 26 + 97)
            else :
                message += i
    return message

def decryptage (chaine: str, decalage: int)-> str:    
    message = ""
    for i in chaine:
        if i == ' ':
            message += i
        else :
            if i.isupper():  # Si la lettre est en minuscule
                message += chr(((ord(i) - 65 ) - decalage) % 26 + 65)
            elif i.islower(): # Si la lettre est en majuscule
                message += chr(((ord(i) - 97 ) - decalage) % 26 + 97)
            else :
                message += i
    return message

choix = int(input("Tapez 1 pour chiffer et 2 pour déchiffer : "))

if choix == 1:
    chaine = input("Entrez une chaîne de caractères à crypter : ")
    decalage = int(input("Entrez la valeur du décalage : "))
    print("Message crypté : ", cryptage(chaine, decalage))
elif choix == 2:
    chaine = input("Entrez une chaîne de caractères à crypter : ")
    decalage = int(input("Entrez la valeur du décalage : "))
    print("Message décrypté : ", decryptage(chaine, decalage))
else :
    print("Choix incorrect.")