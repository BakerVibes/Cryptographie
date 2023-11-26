# Cryptage de César en langage python
# D'abord vous devez choisir l'opération à exécuter (crypter ou décrypter), ensuite vous entrez la valeur du texte à crypter ou décrypter. Et enfin vous entrez la valeur du décalage

def cryptage (chaine: str, decalage: int)-> str:    
    message = ""
    for i in chaine:
        code_ascii = ord(i) + decalage
        message += chr(code_ascii)
    return message

def decryptage (chaine: str, decalage: int)-> str:    
    message = ""
    for i in chaine:
        code_ascii = ord(i) - decalage
        message += chr(code_ascii)
    return message

choix = int(input("Tapez 1 pour chiffer et 2 pour déchiffer : "))
chaine = input("Entrez une chaîne de caractères à crypter : ")
decalage = int(input("Entrez la valeur du décalage : "))

if choix == 1:
    print("Message crypté : ", cryptage(chaine, decalage))
elif choix == 2:
    print("Message décrypté : ", decryptage(chaine, decalage))
