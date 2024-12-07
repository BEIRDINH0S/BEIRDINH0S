from microbit import *
from random import *
import Math

dico = {"scoreB":0,"scoreA":0,"ligneY":0,"start":0}
reactionTime = 1000

#METHODES GENERALES

def countdown():
    """décompte"""
    for i in range(3):
        x = 3-i
        basic.show_number(x)
        pause(500)
    basic.clear_screen()

def ligne_rdm():
    """choisi quelle ligne allumer"""
    dico["ligneY"] = randint(0, 4)
    for count in range(5):
        led.plot(dico["ligneY"], count)
    return

#METHODES MODE TRAINING

def algo_points_training(value) :
    return 1000/(Math.exp(-1.618)*Math.sqrt(value))

def ligne_0_2_4_training():
    """donne des points au joueur en fonction de son temps de réaction si le bouton A est pressé"""
    dico["start"] = input.running_time()
    while True:
        elapsed =  input.running_time() - dico["start"]
        if input.button_is_pressed(Button.A): #si bouton A pressé, score A +1 et arrêt fonction
            dico["scoreA"] = dico["scoreA"] + algo_points_training(elapsed)
            break
        elif elapsed > reactionTime: #si le joueur n'a pas réagit à temps
            basic.clear_screen()
            return "perdu"
    basic.clear_screen()
    return ""

def ligne_1_3_training():
    """le joueur perd s'il presse le bouton A"""
    dico["start"] = input.running_time()
    while True:
        elapsed =  input.running_time() - dico["start"]
        if input.button_is_pressed(Button.A): #si bouton A pressé, le joueur perd
            basic.clear_screen()
            return "perdu"
        elif elapsed > reactionTime: #si le joueur n'a pas réagit
            break
    basic.clear_screen()
    return ""

#METHODES MODE MULTI

def ligne0():
    """si joueur A appuie alors point pour lui sinon si joueur B appuie avant alors -1 pour joueur A"""
    while True:
        if input.button_is_pressed(Button.A): #si bouton A pressé, score A +1 et arrêt fonction
            dico["scoreA"] = dico["scoreA"] + 1
            break
        elif input.button_is_pressed(Button.B): #si bouton B pressé, score A -1 et arrêt fonction
            if dico["scoreA"] > 0:
                dico["scoreA"] = dico["scoreA"] - 1
                break
            else:
                break
    basic.clear_screen()
    return str(dico["scoreA"])

def ligne_1_et_3():
    """-1 pour le joueur qui appuie"""
    dico["start"] = input.running_time()
    while True:
        elapsed =  input.running_time() - dico["start"]
        if input.button_is_pressed(Button.A): #si bouton A pressé, score joueur A -1 et arrêt fonction
            if dico["scoreA"] > 0:
                dico["scoreA"] = dico["scoreA"] - 1
                basic.clear_screen()
                return str(dico["scoreA"])
            else:
                return str(dico["scoreA"])
        elif input.button_is_pressed(Button.B): #si bouton B pressé, score joueur B -1 et arrêt fonction
            if dico["scoreB"] > 0:
                dico["scoreB"] = dico["scoreB"] - 1
                basic.clear_screen()
                return str(dico["scoreB"])
            else:
                return str(dico["scoreB"])
        elif elapsed > reactionTime: #si 2 secondes écoulées, affiche score des 2 joueurs et arrêt de fonction
            break
    basic.clear_screen()
    return str(dico["scoreA"]) + "-" + str(dico["scoreB"])

def ligne2():
    """+1 pour le joueur qui appuie"""
    while True:
        if input.button_is_pressed(Button.A): #si bouton A pressé, score joueur A +1 et arrêt fonction
            dico["scoreA"] = dico["scoreA"] + 1
            basic.clear_screen()
            return str(dico["scoreA"])
        elif input.button_is_pressed(Button.B):#si bouton B pressé, score joueur B +1 et arrêt fonction
            dico["scoreB"] = dico["scoreB"] + 1
            basic.clear_screen()
            return str(dico["scoreB"])

def ligne4():
    """si joueur B appuie alors point pour lui sinon si joueur A appuie avant alors -1 pour joueur A"""
    while True:
        if input.button_is_pressed(Button.B):
            dico["scoreB"] = dico["scoreB"] + 1
            break
        elif input.button_is_pressed(Button.A):
            if dico["scoreB"] > 0:
                dico["scoreB"] = dico["scoreB"] - 1
                break
            else:
                break
    basic.clear_screen()
    return str(dico["scoreB"])


def main():
    """fonction principale"""
    basic.show_string("S")
    while True:
        if input.button_is_pressed(Button.A) : #lance multi
            countdown()
            multi()
            break
        if input.button_is_pressed(Button.B) :#lance training
            countdown()
            training()
            break

def training():
    essai = 0
    while essai < 10:
        ligne_rdm()
        print(dico["ligneY"])
        if dico["ligneY"] in (0, 2, 4):
            ligne = ligne_0_2_4_training()
            essai += 1
        else :
            ligne = ligne_1_3_training()
        basic.show_string(ligne,75)
        if ligne == "perdu":
            break
        pause(500)
        basic.clear_screen()
    basic.show_number(Math.round(dico["scoreA"]), 90)


def multi():
    while dico["scoreA"] < 5 and dico["scoreB"] < 5:
        ligne_rdm()
        if dico["ligneY"] == 0:
            basic.show_string(ligne0())
            pause(500)
        elif dico["ligneY"] == 1:
            basic.show_string(ligne_1_et_3(),75)
            pause(500)
        elif dico["ligneY"] == 2:
            basic.show_string(ligne2())
            pause(500)
        elif dico["ligneY"] == 3:
            basic.show_string(ligne_1_et_3(),75)
            pause(500)
        elif dico["ligneY"] == 4:
            basic.show_string(ligne4())
            pause(500)
        basic.clear_screen()
    if dico["scoreA"] == 5 :
        return basic.show_string("Player A won",75)
    elif dico["scoreB"] == 5 :
        return basic.show_string("Player B won",75)
    
main() #appel de la fonction
