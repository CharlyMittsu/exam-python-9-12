from random import *
from colorama import init
init()
from colorama import Fore, Back, Style
'''
print(Fore.RED + 'some red text', end=" ")
print(Back.GREEN + 'and with a green background')

print(Style.RESET_ALL)
print('back to normal now')

alea = randint(0,9)
print(alea)
'''
partieFinie = False
essais = 8
bibliotheque_mot = ("valise","enfant","propre","foudre","relief","compte","bateau","trappe","suivre","totem")

def Regles():
    print("Dans ce jeu, vous devez deviner un mot dont vous connaissez le nombre de lettre.")
    print("Pour ce faire vous devez entrer un mot du même nombre de lettre.")
    print("Les lettres du mot que vous avez donné seront colorés pour vous indiquer à quel point vous êtes proche de la solution.")
    print("Rouge : la lettre est à la bonne place.")
    print("Jaune : la lettre est mal positionné mais elle se trouve quelque part dans le mot.")
    print("Bleu : le mot ne contient pas cette lettre.")

def randomWord():

    alea = choice(bibliotheque_mot)
    print("vous êtes tombé sur le mot ", Back.GREEN + alea)
    print(Style.RESET_ALL)

    
def search (lettre): #1.5
    

   # lettre = input("entrer la lettre à chercher.")
    nombre = 0
    for i in range (0, len(alea)-1):
        if (lettre==alea[i]):
            position = i+1
            nombre+=1
    if (nombre<1):
        print("Le mot ne contient pas cette lettre.")
    else:
        if(nombre>1):
            print("Cette lettre est apparu ",nombre," fois.")
        else:
            print("La lettre ",lettre," apparait à la ",position,"e position.")



randomWord() #on prend un mot quand la partie commence
while (essais>0 and partieFinie == False):
    #reset
    correct = 0
    print(Style.RESET_ALL)
    
    guess = input("Il vous reste ",essais," essais. Entrez un mot :")
    for i in range (0, len(alea)-1):
        if(guess[i]==alea[i]):
            print(Back.RED + guess[i])
            correct += 1
        else:
            print(Style.RESET_ALL + guess[i])
    if (correct == len(alea)):
        partieFinie = True
    essais = essais-1

if (partieFinie = True):
    print("GG no re, c'était bien ",alea)
else:
    print("Cheh, tu n'as plus d'essais ! Le mot à trouver était ",alea)
input()