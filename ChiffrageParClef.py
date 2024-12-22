

def clearscreen():
    # Efface l'écran en imprimant 50 lignes vides
    for i in range (0,50):
        print("  ")


def coderchr(a,b,lettreAchiffer):
    # Initialise les variables pour l'alphabet et les indices ASCII correspondants
    alphabet = []
    correspondanceASCII = []
    for i in range (65,91):  # Boucle sur les lettres majuscules de l'alphabet (ASCII 65 à 90)
        alphabet.append(chr(i))  # Convertit le code ASCII en caractère et l'ajoute à la liste alphabet

    for i in range (0,26):  # Crée une liste des indices de 0 à 25 correspondant à chaque lettre
        correspondanceASCII.append(i)

    for i in range (0,26):  # Trouve l'indice correspondant à la lettre à chiffrer
        if(lettreAchiffer==alphabet[i]):
            indiceLettreAChiffre = correspondanceASCII[i]  # Sauvegarde l'indice trouvé

    # Applique la formule de chiffrement : (a * indice + b) modulo 26
    indiceLettreChiffre = int((a*indiceLettreAChiffre+b)%26)
    lettreChiffre = alphabet[indiceLettreChiffre]  # Récupère la lettre chiffrée dans l'alphabet
    return(lettreChiffre)  # Retourne la lettre chiffrée


def CoderUnMot():
    # Initialise une liste pour contenir les lettres du mot à coder
    motAcoder = []

    while True:
        # Demande à l'utilisateur de saisir une lettre ou 'fin' pour terminer
        lettre = input("Saisissez votre mot lettre par lettre (ou 'fin' pour terminer) : ")
        if lettre == 'fin':  # Vérifie si l'utilisateur entre 'fin'
            break  # Sort de la boucle
        motAcoder.append(lettre)  # Ajoute la lettre à la liste

    # Affiche le mot à coder en joignant les lettres saisies
    print("Mot à coder :", "".join(motAcoder))

    # Initialise une liste pour contenir les lettres chiffrées
    motCode = []
    for i in range(0, len(motAcoder)):  # Boucle sur chaque lettre du mot
        lettrechiffre = coderchr(a, b, motAcoder[i].upper())  # Chiffre chaque lettre en majuscule
        motCode.append(lettrechiffre)  # Ajoute la lettre chiffrée à la liste
    # Affiche le mot chiffré en joignant les lettres
    print("Mot reconstitué :", "".join(motCode))


# Affiche le menu principal avec deux options
print("   ---Menu Principal---   \n\n1- Coder un caractere \n2- Coder un mot\n\n")
choix = input("Saisie : ")  # Demande à l'utilisateur de choisir une option
if int(choix) == 1 :  # Vérifie si le choix est 1
    clearscreen()  # Efface l'écran (affiche 50 lignes vides)
    # Demande à l'utilisateur les paramètres pour coder un caractère
    a = int(input("Saisissez la valeur de a : "))
    b = int(input("Saisissez la valeur de b : "))
    lettreAchiffer = input("Saisissez la lettre à chiffrer : ")
    print("\n\nLe caractere code est : ")  # Affiche le caractère chiffré
    print(coderchr(a,b,lettreAchiffer.upper()))  # Appelle la fonction coderchr avec les paramètres fournis

elif int(choix) == 2 :  # Vérifie si le choix est 2
    clearscreen()  # Efface l'écran (affiche 50 lignes vides)
    # Demande à l'utilisateur les paramètres pour coder un mot
    a = int(input("Saisissez la valeur de a : "))
    b = int(input("Saisissez la valeur de b : "))
    CoderUnMot()  # Appelle la fonction CoderUnMot
