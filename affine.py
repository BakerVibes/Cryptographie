import math

def cryptage(chaine:str, a:int, b:int) -> str:
     # Faire le cryptage    
    message = ''
    for i in chaine:
        if i.isupper():
            lettre = chr(((a * (ord(i) - 65) + b) % 26) + 65)
        elif i.islower():
            lettre = chr(((a * (ord(i) - 97) + b) % 26) + 97)
        elif i == ' ':
            lettre = i
        message += lettre            
    return message
    
#Entrer la valeur de a
a = int(input("Entrez la valeur du paramètre a (il doit être premier avec 26): "))

# Vérifier si a et 26 sont premiers entre eux
pgcd = math.gcd(a, 26)
if pgcd == 1: # a et 26 sont premiers entre eux
    #Entrer les valeurs de b et du texte à crypter
    b = int(input("Entrez la valeur du paramètre b : "))
    chaine = input("Entrez le texte que vous voulez crypter : ")
    
    #Afficher le message crypté
    print("Message crypté : ",cryptage(chaine, a, b))
else : # a et 26 ne sont pas premiers entre eux
    print("Le nombre ",a, " n'est pas premier avec 26.")
