from microbit import *
from random import *

dico = {'scoreB':0,'scoreA':0,'ligneY':0,'start':0}
def countdown():
    '''décompte'''
    for i in range(3):
        x = 3-i
        basic.show_number(x)
        pause(1000)
    basic.clear_screen()

def ligne_rdm():
    '''choisi quelle ligne allumer'''
    dico['ligneY'] = randint(0, 4)
    for count in range(5):
        led.plot(dico['ligneY'], count)
    return
input.button_is_pressed(Button.A)
def ligne0():
    '''si joueur A appuie alors point pour lui sinon si joueur B appuie avant alors -1 pour joueur A'''
    again = True
    while again:
        if input.button_is_pressed(Button.A) and dico['ligneY'] == 0: #si bouton A pressé, score A +1 et arrêt fonction
            dico['scoreA'] = dico['scoreA'] + 1
            again = False
        elif input.button_is_pressed(Button.B) and dico['ligneY'] == 0: #si bouton B pressé, score A -1 et arrêt fonction
            if dico['scoreA'] > 0:
                dico['scoreA'] = dico['scoreA'] - 1
                again = False
            else:
                again = False
    basic.clear_screen()
    return dico['scoreA']

def ligne1():
    '''-1 pour le joueur qui appuie'''
    again = True
    dico['start'] = input.running_time()
    while again:
        elapsed =  input.running_time() - dico['start']
        if input.button_is_pressed(Button.A) and dico['ligneY'] == 1: #si bouton A pressé, score joueur A -1 et arrêt fonction
            if dico['scoreA'] > 0:
                dico['scoreA'] = dico['scoreA'] - 1
                again = False
                basic.clear_screen()
                return str(dico['scoreA'])
            else:
                again = False
                return str(dico['scoreA'])
        elif input.button_is_pressed(Button.B) and dico['ligneY'] == 1: #si bouton B pressé, score joueur B -1 et arrêt fonction
            if dico['scoreB'] > 0:
                dico['scoreB'] = dico['scoreB'] - 1
                again = False
                basic.clear_screen()
                return str(dico['scoreB'])
            else:
                again = False
                return str(dico['scoreB'])
        elif elapsed > 2000: #si 2 secondes écoulées, affiche score des 2 joueurs et arrêt de fonction
            time = 0
            again = False
    basic.clear_screen()
    return str(dico['scoreA']) + "-" + str(dico['scoreB'])

def ligne2():
    '''+1 pour le joueur qui appuie'''
    again = True
    while again:
        if input.button_is_pressed(Button.A) and dico['ligneY'] == 2 : #si bouton A pressé, score joueur A +1 et arrêt fonction
            dico['scoreA'] = dico['scoreA'] + 1
            again = False
            basic.clear_screen()
            return dico['scoreA']
        elif input.button_is_pressed(Button.B) and dico['ligneY'] == 2 :#si bouton B pressé, score joueur B +1 et arrêt fonction
            dico['scoreB'] = dico['scoreB'] + 1
            again = False
            basic.clear_screen()
            return dico['scoreB']
    return 0

def ligne3():
    '''-1 pour le joueur qui appuie'''
    again = True
    dico['start'] = input.running_time()
    while again:
        elapsed = input.running_time() - dico['start']
        if input.button_is_pressed(Button.A) and dico['ligneY'] == 3:
            if dico['scoreA'] > 0:
                dico['scoreA'] = dico['scoreA'] - 1
                again = False
                basic.clear_screen()
                return str(dico['scoreA'])
            else:
                again = False
                return str(dico['scoreA'])
        elif input.button_is_pressed(Button.B) and dico['ligneY'] == 3:
            if dico['scoreB'] > 0:
                dico['scoreB'] = dico['scoreB'] - 1
                again = False
                basic.clear_screen()
                return str(dico['scoreB'])
            else:
                again = False
                return str(dico['scoreB'])
        elif elapsed > 2000:
            again = False
            time = 0
    basic.clear_screen()
    return str(dico['scoreA']) + "-" + str(dico['scoreB'])

def ligne4():
    '''si joueur B appuie alors point pour lui sinon si joueur A appuie avant alors -1 pour joueur A'''
    again = True
    while again:
        if input.button_is_pressed(Button.B) and dico['ligneY'] == 4:
            dico['scoreB'] = dico['scoreB'] + 1
            again = False
        elif input.button_is_pressed(Button.A) and dico['ligneY'] == 4:
            if dico['scoreB'] > 0:
                dico['scoreB'] = dico['scoreB'] - 1
                again = False
            else:
                again = False
    basic.clear_screen()
    return dico['scoreB']


def main():
    '''fonction principale'''
    play = True
    basic.show_string('Press to play')
    while play:
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            countdown()
            play = False
    while dico['scoreA'] < 5 and dico['scoreB'] < 5:
        ligne_rdm()
        if dico['ligneY'] == 0:
            basic.show_number(ligne0())
            pause(1000)
        elif dico['ligneY'] == 1:
            basic.show_string(ligne1())
            pause(1000)
        elif dico['ligneY'] == 2:
            basic.show_number(ligne2())
            pause(1000)
        elif dico['ligneY'] == 3:
            basic.show_string(ligne3())
            pause(1000)
        elif dico['ligneY'] == 4:
            basic.show_number(ligne4())
            pause(1000)
        basic.clear_screen()
    if dico['scoreA'] == 5 :
        return basic.show_string("Player A won")
    elif dico['scoreB'] == 5 :
        return basic.show_string("Player B won")


main() #appel de la fonction