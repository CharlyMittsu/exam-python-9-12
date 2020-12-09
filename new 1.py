from random import *
from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text', end=" ")
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

'''alea = randint(0,9)
print(alea)'''



def randomWord():
    bibliotheque_mot = ("valise","enfant","propre","foudre","relief","compte","bateau","trappe","suivre","totem")
    alea = choice(bibliotheque_mot)
    print(alea)

randomWord()



input()