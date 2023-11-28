def cryptage(chaine: str, cle: chr, choix: int) -> str:
    # Vérifier le choix de construction de l'alphabet
    if choix == 1:
        # Construire l'alphabet à partir de la lettre
        alphabet = ''
        cle = cle.upper()
        for i in range(26):
            # Appliquer une formule pour créer un alphabet décalé par rapport à la lettre de la clé
            lettre = chr(((ord(cle) + i - 65) % 26) + 65)
            alphabet += lettre
        alphabet = alphabet.upper()
    elif choix == 2:
        # Construire l'alphabet à partir du mot clé
        alphabet = ''
        cle = cle.upper()
        for lettre in cle:
            # Construire un alphabet unique en utilisant les lettres distinctes du mot clé
            if lettre not in alphabet:
                alphabet += lettre
        for i in range(65, 91):
            # Ajouter les lettres restantes de l'alphabet
            lettre = chr(i)
            if lettre not in alphabet:
                alphabet += lettre
        alphabet = alphabet.upper()    

    # Définir le carré de Polybe
    carre = {}
    valeur = 0
    for i in range(26):
        lettre_courante = alphabet[i]
        if lettre_courante != 'J':
            # Associer chaque lettre à ses coordonnées dans le carré de Polybe
            coordonnees = f'{(valeur // 5) + 1}{(valeur % 5) + 1}'
            carre[lettre_courante] = coordonnees
            valeur += 1
        else:
            # 'J' est souvent combiné avec 'I' dans le carré de Polybe
            carre['J'] = carre['I']

    # Chiffrer la chaîne en utilisant le carré de Polybe
    chaine = chaine.upper()
    message = ""
    for i in chaine:
        if i.isalpha():
            # Ajouter les coordonnées du carré de Polybe pour chaque lettre
            if i in carre:
                message += carre[i]
        else:
            # Ajouter directement les caractères non alphabétiques
            message += i
    return message

def decryptage(code: str, cle: str, choix: int) -> str:
    # Vérifier le choix de construction de l'alphabet
    if choix == 1:
        # Construire l'alphabet à partir de la lettre
        alphabet = ''
        for i in range(26):
            # Appliquer une formule pour créer un alphabet décalé par rapport à la lettre de la clé
            letter = chr(((ord(cle) + i - 65) % 26) + 65)
            alphabet += letter
        alphabet = alphabet.upper()
    elif choix == 2:
        # Construire l'alphabet à partir du mot clé
        alphabet = ''
        cle = cle.upper()
        for lettre in cle:
            # Construire un alphabet unique en utilisant les lettres distinctes du mot clé
            if lettre not in alphabet:
                alphabet += lettre
        for i in range(65, 91):
            # Ajouter les lettres restantes de l'alphabet
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
            # Associer chaque coordonnée à sa lettre correspondante dans l'inverse du carré de Polybe
            coordonnees = f'{(valeur // 5) + 1}{(valeur % 5) + 1}'
            inverse_carre[coordonnees] = lettre_courante
            valeur += 1

    # Déchiffrer le code en utilisant l'inverse du carré de Polybe
    decrypted_message = ""
    i = 0
    while i < len(code):
        if code[i].isdigit() and i+1 < len(code):
            coordonnees = code[i:i+2]
            if coordonnees in inverse_carre:
                decrypted_message += inverse_carre[coordonnees]
            else:
                decrypted_message += code[i:i+2]  # Ajouter les caractères originaux
            i += 2
        else:
            decrypted_message += code[i]  # Ajouter le caractère original
            i += 1

    return decrypted_message

# Demander à l'utilisateur s'il souhaite chiffrer ou déchiffrer
choix = int(input("Tapez 1 pour chiffrer et 2 pour déchiffrer : "))

# Si l'utilisateur choisit de chiffrer
if choix == 1:
    # Demander à l'utilisateur s'il veut chiffrer avec une lettre ou un mot clé
    choix = int(input("Tapez 1 pour chiffrer à partir d'une lettre et 2 pour chiffrer à partir d'un mot clé : "))
    
    if choix == 1:
        # Demander à l'utilisateur la chaîne à chiffrer et la lettre
        chaine = input("Entrez une chaîne de caractères à crypter : ")
        lettre = input("Entrez la lettre de début du carré de polype : ")
        # Afficher le message chiffré
        print("Message chiffré : ", cryptage(chaine, lettre, choix))
    
    elif choix == 2:
        # Demander à l'utilisateur la chaîne à chiffrer et le mot clé
        chaine = input("Entrez une chaîne de caractères à crypter : ")
        mot = input("Entrez le mot clé du carré de polype : ")
        # Afficher le message chiffré
        print("Message chiffré : ", cryptage(chaine, mot, choix))
    
    else:
        print("Choix incorrect.")

# Si l'utilisateur choisit de déchiffrer
elif choix == 2:
    # Demander à l'utilisateur s'il veut déchiffrer avec une lettre ou un mot clé
    choix = int(input("Tapez 1 pour déchiffrer à partir d'une lettre et 2 pour déchiffrer à partir d'un mot clé : "))
    
    if choix == 1:
        # Demander à l'utilisateur le code à déchiffrer et la lettre de début
        code = input("Entrez le code à décrypter : ")
        lettre = input("Entrez la lettre de début du carré de polype : ")
        # Afficher le message déchiffré
        print("Message déchiffré : ", decryptage(code, lettre, choix))
    
    elif choix == 2:
        # Demander à l'utilisateur le code à déchiffrer et le mot clé
        code = input("Entrez le code à décrypter : ")
        mot = input("Entrez le mot clé du carré de polype : ")
        # Afficher le message déchiffré
        print("Message déchiffré : ", decryptage(code, mot, choix))
    
    else:
        print("Choix incorrect.")

else:
    print("Choix incorrect.")
