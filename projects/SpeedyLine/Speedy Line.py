from microbit import *
from random import *

dico = {'scoreB':0,'scoreA':1,'ligneY':0,'start':0}

def countdown():
    '''décompte'''
    for i in range(3):
        x = 3-i
        display.show(x)
        sleep(1000)
    display.clear()

def ligne_rdm():
    '''choisi quelle ligne allumer'''
    dico['ligneY'] = randint(0, 4)
    for count in range(5):
        display.set_pixel(dico['ligneY'], count,9)
    return

def ligne0():
    '''si joueur A appuie alors point pour lui sinon si joueur B appuie avant alors -1 pour joueur A'''
    again = True
    while again:
        if button_a.is_pressed() and dico['ligneY'] == 0: #si bouton A pressé, score A +1 et arrêt fonction
            dico['scoreA'] = dico['scoreA'] + 1
            again = False
        elif button_b.is_pressed() and dico['ligneY'] == 0: #si bouton B pressé, score A -1 et arrêt fonction
            if dico['scoreA'] > 0:
                dico['scoreA'] = dico['scoreA'] - 1
                again = False
            else:
                again = False
    display.clear()
    return dico['scoreA']

def ligne1():
    '''-1 pour le joueur qui appuie'''
    again = True
    dico['start'] =  running_time()
    while again:
        elapsed =  running_time() - dico['start']
        if button_a.is_pressed() and dico['ligneY'] == 1: #si bouton A pressé, score joueur A -1 et arrêt fonction
            if dico['scoreA'] > 0:
                dico['scoreA'] = dico['scoreA'] - 1
                again = False
                display.clear()
                return str(dico['scoreA'])
            else:
                again = False
                return str(dico['scoreA'])
        elif button_b.is_pressed() and dico['ligneY'] == 1: #si bouton B pressé, score joueur B -1 et arrêt fonction
            if dico['scoreB'] > 0:
                dico['scoreB'] = dico['scoreB'] - 1
                again = False
                display.clear()
                return str(dico['scoreB'])
            else:
                again = False
                return str(dico['scoreB'])
        elif elapsed > 2000: #si 2 secondes écoulées, affiche score des 2 joueurs et arrêt de fonction
            time = 0
            again = False
    display.clear()
    return str(dico['scoreA']) + "-" + str(dico['scoreB'])

def ligne2():
    '''+1 pour le joueur qui appuie'''
    again = True
    while again:
        if button_a.is_pressed() and dico['ligneY'] == 2 : #si bouton A pressé, score joueur A +1 et arrêt fonction
            dico['scoreA'] = dico['scoreA'] + 1
            again = False
            display.clear()
            return dico['scoreA']
        elif button_b.is_pressed() and dico['ligneY'] == 2 :#si bouton B pressé, score joueur B +1 et arrêt fonction
            dico['scoreB'] = dico['scoreB'] + 1
            again = False
            display.clear()
            return dico['scoreB']
    return 0

def ligne3():
    '''-1 pour le joueur qui appuie'''
    again = True
    dico['start'] = running_time()
    while again:
        elapsed = running_time() - dico['start']
        if button_a.is_pressed() and dico['ligneY'] == 3:
            if dico['scoreA'] > 0:
                dico['scoreA'] = dico['scoreA'] - 1
                again = False
                display.clear()
                return str(dico['scoreA'])
            else:
                again = False
                return str(dico['scoreA'])
        elif button_b.is_pressed() and dico['ligneY'] == 3:
            if dico['scoreB'] > 0:
                dico['scoreB'] = dico['scoreB'] - 1
                again = False
                display.clear()
                return str(dico['scoreB'])
            else:
                again = False
                return str(dico['scoreB'])
        elif elapsed > 2000:
            again = False
            time = 0
    display.clear()
    return str(dico['scoreA']) + "-" + str(dico['scoreB'])

def ligne4():
    '''si joueur B appuie alors point pour lui sinon si joueur A appuie avant alors -1 pour joueur A'''
    again = True
    while again:
        if button_b.is_pressed() and dico['ligneY'] == 4:
            dico['scoreB'] = dico['scoreB'] + 1
            again = False
        elif button_a.is_pressed() and dico['ligneY'] == 4:
            if dico['scoreB'] > 0:
                dico['scoreB'] = dico['scoreB'] - 1
                again = False
            else:
                again = False
    display.clear()
    return dico['scoreB']

def main():
    '''fonction principale'''
    play = True
    display.scroll('Press to play')
    while play:
        if button_a.is_pressed() or button_b.is_pressed():
            countdown()
            play = False
    while dico['scoreA'] < 5 and dico['scoreB'] < 5:
        ligne_rdm()
        if dico['ligneY'] == 0:
            display.show(ligne0())
            sleep(1000)
        elif dico['ligneY'] == 1:
            display.show(ligne1())
            sleep(1000)
        elif dico['ligneY'] == 2:
            display.show(ligne2())
            sleep(1000)
        elif dico['ligneY'] == 3:
            display.show(ligne3())
            sleep(1000)
        elif dico['ligneY'] == 4:
            display.show(ligne4())
            sleep(1000)
        display.clear()
    if dico['scoreA'] == 5 :
        return display.scroll("Player A won")
    elif dico['scoreB'] == 5 :
        return display.scroll("Player B won")


main() #appel de la fonction