#I have also made changes here - will need to ouput changes to rest of files, 
#files changed;


#here i am going to test bringing all our work togetehr
#Start with Title Screen
import cmd
import sys
import os
import time
import random
import textwrap

os.system('mode con: cols=190 lines=45')

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
                    
def credits():#credits for when you die and or chose them at the begining
    clrscrn()
    print ("Thank you for playing our game, this is our first attempt and we have no prior coding experience.\n\n\nA lot of help was gathered from github, youtube, x3 and stackoverflow.\n\n\nBattle Mechanics made by Jason Mutter\nLeveling System made by Tomas Keech\nStory made by Jason Mutter\nRoom Design made by Tomas Keech\n\nWe both worked very hard on this little game and we hope you enjoy it")
    back = input ("\n\n\nPress Enter to return to Title Screen, Or type exit to exit")
    while 0 == 0 and back != 0:
        if back == (""):
            clrscrn()
            title_screen()
        elif back == ("exit") or back == ("Exit"):
            os.system (exit)
        else:
            print("Press Enter to return to Title Screen")
            back = 0
            back = input()

def battle_sequence(enemylist,char,inventory):

#choose the random enemy and set their
    enemy_pick(enemylist,char)

#define local variables for the player stats to be used here for ease
    HP = char["HP"]
    ATK = char["ATK"]
    DEF = char["DEF"]

    global ehp
    global eatk
    global edef
    global expgain

    ehp = epick["ehp"]
    eatk = epick["eatk"]
    edef = epick["edef"]
    expgain = epick["expgain"]

    ehp *= char["LVL"]
    eatk *= char["LVL"]
    edef *= char["LVL"]
    expgain *= char["LVL"]

#making a round counter for the battle not used fully yet
    Battle_round = 0

#pick weather the player or opponant will go first on 1 the player will go first
    battle_start_modifier = random.randint(0,1)

#battle choice is the loop controaler. 1 is replay, 0 is next step
   
    Battle_choice = 5
    if battle_start_modifier == 0:
        typing("\nYou got the jump on your opponent!\n\n")
#player round 1 attack ***********************************************************************************************************************************************************************
        while Battle_choice != 0:
            roundehp = ehp
#print the battle state
            print("PLAYERS TURN\n")
            time.sleep(1)
            print("Enemy HP:        " + str(ehp) + "/" + str(epick["ehp"]))
            time.sleep(0.5)
            print("\nPlayer HP:       " + str(HP) + "/" + str(char["HP"]))
            time.sleep(0.5)
            print("Player Armour:   " + str(DEF) + "/" + str(char["DEF"]))
            time.sleep(0.5)
            print("\nChoose your action:")
            time.sleep(0.5)
            print("1 Attack         " + str(ATK))
            print("2 Defend         " + str(DEF))
            print("3 Attack Potion  " + str(inventory["ATKpotion"]))
            print("4 Health Potion  " + str(inventory["HPpotion"])+"\n\n")
            Battle_choice = input()
#attack action, take damage away from defense then add defense
            if Battle_choice == "1":
                ATK += random.randint(-2,2)
                if edef < ATK:
                    edef -= ATK
                    ehp += edef
                elif edef > ATK:
                    edef -= ATK
                    typing("Your attack was blocked.\n")
                else: 
                    ehp -= ATK
                if edef < 0 :
                    edef = 0
                    typing("You broke through your opponents armour\n")
                print("The Enemy lost " + str(roundehp - ehp)+" HP.\n")
                ATK = char["ATK"]
                Battle_choice = 0
#Defense action calculater
            elif Battle_choice == "2":
                DEF += round(0.7 * char["DEF"])
                Battle_choice = 0
                if DEF > char["DEF"]:
                    DEF = char["DEF"]
                    typing("Your defence went up to "+str(DEF))
#take an attack potion stackable
            elif Battle_choice == "3":
                if inventory["ATKpotion"] > 0:
                    ATK += round(0.5*ATK)
                    typing("You gain " + str(ATK - char["ATK"]) + " attack for the rest of this battle\n")
                    inventory["ATKpotion"] -=1
                    Battle_choice = 0
                else:
                    clrscrn()
                    print("Out of attack potions")
                    time.sleep(1)
                    clrscrn()
                    Battle_choice = 5
#take a hp potion
            elif Battle_choice == "4":
                if HP == char["HP"]:
                    typing("You are already at max health")
                    Battle_choice = 5
                    clrscrn()
                else:
                    if inventory["HPpotion"] > 0:
                        befor_potionHP = HP
                        HP += round(0.8*char["HP"])
                        if HP > char["HP"]:
                            HP = char["HP"]
                        typing("You gain " + str(HP - befor_potionHP) + " HP from the potion.")
                        inventory["HPpotion"] -=1
                        Battle_choice = 0
                    else:
                        clrscrn()
                        print("Out of HP potions")
                        time.sleep(1)
                        clrscrn()
                        Battle_choice = 5
        
    if 0 == 0:
#this only runs if the randomiser calls for opponent to go first
        if battle_start_modifier == 1:
            typing("\nYour Opponent got the jump on you!\n\n")
        while ehp > 0 and HP >0:                                
#enemy turn in while function ***********************************************************************************************************************************************************
            Battle_round += 1
            roundehp = ehp
            roundHP = HP
            typing("OPPONENTS TURN\n")
            time.sleep(1)
            print("Enemy HP:        " + str(ehp) + "/" + str(epick["ehp"]))
            time.sleep(0.5)
            print("\nPlayer HP:       " + str(HP) + "/" + str(char["HP"]))
            time.sleep(0.5)
            print("Player Armour:   " + str(DEF) + "/" + str(char["DEF"])+"\n\n")
            time.sleep(0.5)
            opponent_randomiser1 = random.randint(0,1)
            if opponent_randomiser1 == 0:
                opponent_randomiser2 = random.randint(0,1)
                if opponent_randomiser2 == 0:
#enemy attack function
                    typing(epickname + " is attacking!\n")                 
                    eatk += random.randint(-2,2)
                    if DEF < eatk:
                        DEF -= eatk
                        HP += DEF
                    elif DEF > eatk:
                        DEF -= eatk
                        typing("You blocked their attack.\n")
                    else: 
                        HP -= eatk
                    if DEF < 0 :
                        DEF = 0
                        typing("Your opponent broke through your armour\n")
                    print("You lost " + str(roundHP - HP)+" HP.\n")
                    eatk = epick["eatk"]
                else:
#enemy defense function
                    typing(epickname + " is defending!")
                    edef += round(0.7 * epick["edef"])
                    if edef > epick["edef"]:
                        edef = epick["edef"]
            else:
#enemy defense function
                if edef == 0 and HP > eatk-5:
                    typing(epickname + " is defending!")
                    edef += round(0.7 * epick["edef"])
                    if edef > epick["edef"]:
                        edef = epick["edef"]
                else:
#enemy attack function
                    typing(epickname + " is attacking!\n")
                    eatk += random.randint(-2,2)
                    if DEF < eatk:
                        DEF -= eatk
                        HP += DEF
                    elif DEF > eatk:
                        DEF -= eatk
                        typing("You blocked their attack.\n")
                    else: 
                        HP -= eatk
                    if DEF < 0 :
                        DEF = 0
                        typing("Your opponent broke through your armour\n")
                    print("You lost " + str(roundHP - HP)+" HP.\n")
                    eatk = epick["eatk"]
            Battle_choice = 5
            
            if HP > 0 :
#players turn in While loop *************************************************************************************************************************************************
                while Battle_choice != 0: 
                    time.sleep(3)
                    clrscrn()
                    typing("PLAYERS TURN\n")
                    time.sleep(1)
                    print("Enemy HP:        " + str(ehp) + "/" + str(epick["ehp"]))
                    time.sleep(0.5)
                    print("\nPlayer HP:       " + str(HP) + "/" + str(char["HP"]))
                    time.sleep(0.5)
                    print("Player Armour:   " + str(DEF) + "/" + str(char["DEF"]))
                    time.sleep(0.5)
                    print("\nChoose your action:")
                    time.sleep(0.5)
                    print("1 Attack         " + str(ATK))
                    print("2 Defend         " + str(DEF))
                    print("3 Attack Potion  " + str(inventory["ATKpotion"]))
                    print("4 Health Potion  " + str(inventory["HPpotion"])+"\n")
                    Battle_choice = input()
#attack action, take damage away from defense then add defense
                    if Battle_choice == "1":
                        ATK += random.randint(-2,2)
                        if edef < ATK:
                            edef -= ATK
                            ehp += edef
                        elif edef > ATK:
                            edef -= ATK
                            typing("Your attack was blocked.\n")
                        else: 
                            ehp -= ATK
                        if edef < 0 :
                           edef = 0
                           typing("You broke through your opponents armour\n")
                        print("The Enemy lost " + str(roundehp - ehp)+" HP.")
                        ATK = char["ATK"]
                        Battle_choice = 0
#Defense calculater
                    elif Battle_choice == "2":
                        DEF += round(0.7 * char["DEF"])
                        Battle_choice = 0
                        if DEF > char["DEF"]:
                            DEF = char["DEF"]
                        typing("Your defence went up to "+str(DEF))
#take an attack potion stackable
                    elif Battle_choice == "3":
                        if inventory["ATKpotion"] > 0:
                            ATK += round(0.5*ATK)
                            typing("You gain " + str(ATK - char["ATK"]) + " attack for the rest of this battle\n")
                            inventory["ATKpotion"] -=1
                            Battle_choice = 0
                        else:
                            clrscrn()
                            print("Out of attack potions")
                            time.sleep(1)
                            clrscrn()
                            Battle_choice = 5
#take a hp potion
                    elif Battle_choice == "4":
                        if HP == char["HP"]:
                            typing("You are already at max health")
                            Battle_choice = 5
                            clrscrn()
                        else:
                            if inventory["HPpotion"] > 0:
                                befor_potionHP = HP
                                HP += round(0.8*char["HP"])
                                if HP > char["HP"]:
                                    HP = char["HP"]
                                typing("You gain " + str(HP - befor_potionHP) + " HP from the potion.")
                                inventory["HPpotion"] -=1
                                Battle_choice = 0
                            else:
                                print("Out of HP potions")
                                time.sleep(1)
                                clrscrn()
                                Battle_choice = 5
                    clrscrn()

#battle should be finished if the code reaches this comment

        if char['HP'] > 0:
            clrscrn()
            typing("You have provailed in this battle!\n")
            time.sleep(1)
            win = 1
            char['XP'] += expgain
            level(char)
        else:
            typing ("You have been slain")
            time.sleep(2)
            clrscrn()
            endscr()






































#Dictionaries start here
#base char stats
char = {'LVL': 1,
        'XP' : 0,
        'LVLNEXT' : 10,
        'ATK': 10,
         'DEF': 10,
         'HP' : 10}

#enemy base stats
enemylist = {
    "Imp"    : {'ehp':10, 'eatk':4, 'edef':2, 'expgain':13},
    "Ogre"   : {'ehp':15, 'eatk':11, 'edef':12, 'expgain':13},
    "Dwarf"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Tiny Hands" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Giant"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Goblin" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Ghoul"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Psycho" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13}}

#inventory
inventory = {'ATKpotion': 10,
        'HPpotion': 10}




























































































































































































































































title_screen()
