from random import *
from colorama import init
init()
from colorama import Fore, Back, Style
'''
print(Fore.RED + 'some red text', end=" ")
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

alea = randint(0,9)
print(alea)
'''



def randomWord():
    bibliotheque_mot = ("valise","enfant","propre","foudre","relief","compte","bateau","trappe","suivre","totem")
    alea = choice(bibliotheque_mot)
    print("vous êtes tombé sur le mot ", Back.GREEN + alea)
    print(Style.RESET_ALL)

def search (): #1.0
    
    randomWord()
    lettre = input("entrer la lettre à chercher.")
    nombre = 0
    for i in range (0, len(alea)-1):
        if (lettre==alea[i]):
            position = i+1
            nombre+=1
    if (nombre<1):
        print("Le mot ne contient pas cette lettre.")
    else:
        if(nombre>1):
            print("cette lettre est apparu ",nombre," fois.")
        else:
            print("la lettre ",lettre," apparait à la ",position,"e position.")
        
search()

input()