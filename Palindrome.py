import string

machaine="Esope reste ici et se repose"


def SuppEspace(machaine):
    # ma chaine concatenée suppression des espaces
    newChaine = machaine.replace(" ","")
    return newChaine

def suppressionChar(machaine):
    machaine = SuppEspace(machaine)
    machaine = "".join([i.lower() for i in machaine if i.isalnum()])
    return machaine

#machaine =  suppressionChar(machaine)

def inverseString(machaine):
    machaine = suppressionChar(machaine)
    return machaine[::-1]

def isPalindrome(machaine):
    if suppressionChar(machaine) == inverseString(machaine) :
        print(" est un palindrome ")
    else :
       print(" n'est pas un palindrome ")

  

isPalindrome(machaine)
