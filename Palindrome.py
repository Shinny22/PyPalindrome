



import string


def AfficheParametre(maChaine):
    print(maChaine)

machaine="engage le jeu que je le gagne?!"
AfficheParametre(machaine)

def SuppEspace(machaine):

    # ma chaine concatenée suppression des espaces
    newChaine=machaine.replace(" ","")
    print(newChaine)

    # suppression des caractères speciaux

    # Mappage des caratères speciaux grace à la fonction maketrans()
    # string.punction est l'ensemble des caractère speciaux definit dans le module string
    chaineSansCaractere=str.maketrans("","",string.punctuation)
    chaineTranslate=machaine.translate(chaineSansCaractere)
    print(chaineTranslate)
   


    # ma chaine inversée
    inverseChaine=chaineTranslate[ : :-1]
    print(inverseChaine)

    #  ma chaine inversée réarrangée
    chaineFinale=inverseChaine.replace(""," ")
    print(chaineFinale)

    # sep=" "
    # inverseChaine=sep.join(inverseChaine)
     
    # Test de conformité
    if (chaineFinale==machaine):
        print(machaine,"est un palindrome")
    else:
        print(machaine,"n'est un palindrome")

SuppEspace(machaine)