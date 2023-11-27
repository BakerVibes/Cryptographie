def cryptageLettre (chaine:str, lettre:str)->str:
    
    # Construire l'alphabet à partir de la lettre
    alphabet = ''
    lettre = lettre.upper()
    for i in range(26):
        letter = chr(((ord(lettre) + i - 65) % 26) + 65)
        alphabet += letter
    alphabet = alphabet.upper()    

    # Définir le carré de polybe
    carre = {}
    valeur = 0
    for i in range(26):
        lettre_courante = alphabet[i]
        if lettre_courante != 'J':
            coordonnees = f'{(valeur // 5) + 1}{(valeur % 5) + 1}'
            carre[lettre_courante] = coordonnees
            valeur += 1
        else:
            carre['J'] = carre['I']
    
    # Faire le cryptage
    chaine = chaine.upper()
    message = ""
    for i in chaine:
        if i in carre:
            message += carre[i]
        elif i == ' ':
            message = i
    return message

def cryptageMot(chaine: str, mot: str) -> str:

    # Construire l'alphabet à partir du mot clé
    alphabet = ''
    mot = mot.upper()    
    for lettre in mot:
        if lettre not in alphabet:
            alphabet += lettre
    for i in range(65, 91):
        lettre = chr(i)
        if lettre not in alphabet:
            alphabet += lettre
    alphabet = alphabet.upper()    

    # Définir le carré de polybe
    carre = {}
    valeur = 0
    for i in range(26):
        lettre_courante = alphabet[i]
        if lettre_courante != 'J':
            coordonnees = f'{(valeur // 5) + 1}{(valeur % 5) + 1}'
            carre[lettre_courante] = coordonnees
            valeur += 1
        else:
            carre['J'] = carre['I']

    # Faire le cryptage
    chaine = chaine.upper()
    message = ""
    for i in chaine:
        if i in carre:
            message += carre[i]
        elif i == ' ':
            message = i
    return message

def decryptageLettre(code: str, lettre: str) -> str:

    # Construire l'alphabet à partir de la lettre
    alphabet = ''
    for i in range(26):
        letter = chr(((ord(lettre) + i - 65) % 26) + 65)
        alphabet += letter
    alphabet = alphabet.upper()

    # Définir l'inverse du carré de Polybe
    inverse_carre = {}
    valeur = 0
    for i in range(26):
        lettre_courante = alphabet[i]
        if lettre_courante != 'J':
            coordonnees = f'{(valeur // 5) + 1}{(valeur % 5) + 1}'
            inverse_carre[coordonnees] = lettre_courante
            valeur += 1
                        
    # Faire le décryptage
    decrypted_message = ""
    i = 0
    while i < len(code):
        coordonnees = code[i:i+2]
        decrypted_message += inverse_carre[coordonnees]
        i += 2
    return decrypted_message


def decryptageMot(message: str, mot: str) -> str:
    
    # Construire l'alphabet à partir du mot clé
    alphabet = ''
    mot = mot.upper()
    for lettre in mot:
        if lettre not in alphabet:
            alphabet += lettre
    for i in range(65, 91):
        lettre = chr(i)
        if lettre not in alphabet:
            alphabet += lettre
    alphabet = alphabet.upper()

    # Définir l'inverse du carré de Polybe
    inverse_carre = {}
    valeur = 0
    for i in range(26):
        lettre_courante = alphabet[i]
        if lettre_courante != 'J':
            coordonnees = f'{(valeur // 5) + 1}{(valeur % 5) + 1}'
            inverse_carre[coordonnees] = lettre_courante
            valeur += 1

    # Faire le décryptage
    decrypted_message = ""
    i = 0
    while i < len(message):
        coordonnees = message[i:i+2]
        decrypted_message += inverse_carre[coordonnees]
        i += 2
    return decrypted_message

choix = int(input("Tapez 1 pour chiffer et 2 pour déchiffer : "))

if choix == 1:
    choix = int(input("Tapez 1 pour chiffer à partir d'une lettre et 2 pour chiffer à partir d'un mot clé : "))
    if choix == 1:
        chaine = input("Entrez une chaîne de caractères à crypter : ")
        lettre = input("Entrez la lettre de début du carré de polype : ")
        print("Message crypté : ", cryptageLettre(chaine, lettre))
    elif choix == 2:
        chaine = input("Entrez une chaîne de caractères à crypter : ")
        mot = input("Entrez le mot clé du carré de polype : ")
        print("Message crypté : ", cryptageMot(chaine, mot))
    else :
        print("Choix incorrect.")
elif choix == 2:
    choix = int(input("Tapez 1 pour déchiffer à partir d'une lettre et 2 pour déchiffer à partir d'un mot clé : "))
    if choix == 1:
        code = input("Entrez le code à décrypter : ")
        lettre = input("Entrez la lettre de début du carré de polype : ")
        print("Message décrypté : ", decryptageLettre(code, lettre))
    elif choix == 2:
        code = input("Entrez le code à décrypter : ")
        mot = input("Entrez le mot clé du carré de polype : ")
        print("Message décrypté : ", decryptageMot(code, mot))
    else :
        print("Choix incorrect.")
else :
    print("Choix incorrect.")
