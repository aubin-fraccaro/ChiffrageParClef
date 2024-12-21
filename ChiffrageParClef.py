from os import popen





def coderchr(a,b,lettreAchiffer):
    alphabet = []
    correspondanceASCII = []
    for i in range (65,91):
        alphabet.append(chr(i))

    for i in range (0,26):
        correspondanceASCII.append(i)

    for i in range (0,26):
        if(lettreAchiffer==alphabet[i]):
            indiceLettreAChiffre = correspondanceASCII[i]

    indiceLettreChiffre = int((a*indiceLettreAChiffre+b)%26)
    lettreChiffre = alphabet[indiceLettreChiffre]
    return(lettreChiffre)



def CoderUnMot():
    motAcoder = []

    while True:
        lettre = input("Saisissez votre mot lettre par lettre (ou 'fin' pour terminer) : ")
        if lettre == 'fin':  # Vérifie si l'utilisateur entre 'fin'
            break  # Sort de la boucle
        motAcoder.append(lettre)  # Ajoute la lettre à la liste

    print("Mot à coder :", "".join(motAcoder))  # Assemble les lettres en une chaîne et affiche le mot

    motCode = []
    for i in range(0, len(motAcoder)):
        lettrechiffre = coderchr(a, b, motAcoder[i])
        motCode.append(lettrechiffre)
    print("Mot reconstitué :", "".join(motCode))  # Assemble les lettres en une chaîne et affiche le mot



print("   ---Menu Principal---   \n\n1- Coder un caractere \n2- Coder un mot\n\n")
choix = input("Saisie : ")
if int(choix) == 1 :
    a = int(input("Saisissez la valeur de a : "))
    b = int(input("Saisissez la valeur de b : "))
    lettreAchiffer = input("Saisissez la lettre à chiffrer")
    print("Le caractere code est : ")
    print(coderchr(a,b,lettreAchiffer))

elif int(choix) == 2 :
    a = int(input("Saisissez la valeur de a : "))
    b = int(input("Saisissez la valeur de b : "))
    CoderUnMot()











