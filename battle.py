import sys
import time
import os
import random
import pip

def clrscrn():
    if os.name == 'posix':
        _=os.system("clear")
    else:
        _=os.system('cls')

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def enemy_pick(enemylist,char):
    #picks a random enemy from the dictionary enemylist
    enemypick = (random.choice(list(enemylist.items())))

    global epickname
    global epick

    epickname = enemypick[0]
    epick = dict(enemypick[1])

#epickname shows the chosen enemys name
#epick is the chosen enemys stats as a dictionary

#ascii text generator to change if needed https://patorjk.com/software/taag/#p=display&f=Big%20Chief&t=Tiny%20Hands
    Imp_string = '''
______________________________________________
  ______                     __               
    /      /                 /                
---/------/__----__---------/----_--_------__-
  /      /   ) /___)       /    / /  )   /   )
_/______/___/_(___ _____ _/_ __/_/__/___/___/_
                                       /      
                                      /       
'''

    Ogre_string = '''
___________________________________________________
  ______                     __                    
    /      /               /    )                  
---/------/__----__-------/----/----__---)__----__-
  /      /   ) /___)     /    /   /   ) /   ) /___)
_/______/___/_(___ _____(____/___(___/_/_____(___ _
                                    /              
                                (_ /               
'''

    Dwarf_string = '''
___________________________________________________________
  ______                   _____                         _ 
    /      /               /    )                      /  `
---/------/__----__-------/----/-----------__---)__--_/__--
  /      /   ) /___)     /    /  | /| /  /   ) /   ) /     
_/______/___/_(___ _____/____/___|/_|/__(___(_/_____/______
                                                           
                                                           
'''

    Bird_string = '''
_______________________________________________________________
  ______                       _     _                         
    /      ,                   /    /                    /     
---/-----------__-------------/___ /-----__----__----__-/---__-
  /      /   /   ) /   /     /    /    /   ) /   ) /   /   (_ `
_/______/___/___/_(___/_____/____/____(___(_/___/_(___/___(__)_
                     /                                         
                 (_ /                                          
'''

    Giant_string ='''
______________________________________________________
  ______                     __                       
    /      /               /    )   ,                 
---/------/__----__-------/-------------__----__--_/_-
  /      /   ) /___)     /  --,   /   /   ) /   ) /   
_/______/___/_(___ _____(____/___/___(___(_/___/_(_ __
                                                      
                                                      
'''

    Goblin_string = '''
___________________________________________________________
  ______                     __                            
    /      /               /    )         /     /   ,      
---/------/__----__-------/---------__---/__---/--------__-
  /      /   ) /___)     /  --,   /   ) /   ) /   /   /   )
_/______/___/_(___ _____(____/___(___/_(___/_/___/___/___/_
                                                           
                                                          
'''

    Ghoul_string = '''
________________________________________________________
  ______                     __                         
    /      /               /    )   /                  /
---/------/__----__-------/--------/__----__----------/-
  /      /   ) /___)     /  --,   /   ) /   ) /   /  /  
_/______/___/_(___ _____(____/___/___/_(___/_(___(__/___
                                                        
                                                        
'''

    Psycho_string = '''
______________________________________________________________
  ______                   ____                               
    /      /               /    )                    /        
---/------/__----__-------/____/---__----------__---/__----__-
  /      /   ) /___)     /        (_ ` /   / /   ' /   ) /   )
_/______/___/_(___ _____/________(__)_(___/_(___ _/___/_(___/_
                                         /                    
                                     (_ /                     
'''


    if epickname == "Imp":
        print(Imp_string)
        print("\n\n\n")
        print("description")
    elif epickname == "Ogre":
        print(Ogre_string)
        print("\n\n\n")
        print("description")
    elif epickname == "Dwarf":
        print(Dwarf_string)
        print("\n\n\n")
        print("description")
    elif epickname == "Tiny Hands":
        print(Bird_string)
        print("\n\n\n")
        print("description")
    elif epickname == "Giant":
        print(Giant_string)
        print("\n\n\n")
        print("description")
    elif epickname == "Goblin":
        print(Goblin_string)
        print("\n\n\n")
        print("description")
    elif epickname == "Ghoul":
        print(Ghoul_string)
        print("\n\n\n")
        print("description")
    elif epickname == "Psycho":
        print(Psycho_string)
        print("\n\n\n")
        print("description")

#setting enemy stats as variables for easy access


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

    #making a round counter for the battle
    Battle_round = 0

    #pick weather the player or opponant will go first on 1 the player will go first
    battle_start_modifier = 1 #random.randint(1,2)


    #battle choice is the loop controaler. 1 is replay, 0 is next step
   
    Battle_choice = 1
    if battle_start_modifier == 1:
        typing("\nYou got the jump on your opponent!\n\n")
        while Battle_choice != 0:                               #player round 1 attack
            roundehp = ehp
            #print the battle state
            print("PLAYERS TURN\n")
            time.sleep(1)
            print("Enemy HP:        " + str(ehp) + "/" + str(epick["ehp"]))
            time.sleep(0.5)
            print("Player HP:       " + str(HP) + "/" + str(char["HP"]))
            time.sleep(0.5)
            print("Player Armour:   " + str(DEF) + "/" + str(char["DEF"]))
            time.sleep(0.5)
            print("\nChoose your action:")
            time.sleep(0.5)
            print("1 Attack         " + str(ATK))
            print("2 Defend         " + str(DEF))
            print("3 Attack Potion  " + str(inventory["ATKpotion"]))
            print("4 Health Potion  " + str(inventory["HPpotion"]))
            Battle_choice = input()
            #attack action, take damage away from defense then add defense
            if Battle_choice == "1":
                ATK += random.randint(-2,2)
                if edef < ATK:
                    edef -= ATK
                    ehp += edef
                elif edef > ATK:
                    edef -= ATK
                else: 
                    ehp -= ATK
                if edef < 0 :
                    edef = 0
                    typing("You broke through your opponents armour")
                print("The Enemy lost " + str(roundehp - ehp)+"HP.")
                Battle_choice = 0
            elif Battle_choice == "2":
                DEF += round(0.5 * char["DEF"])
                Battle_choice = 0
                if DEF > char["DEF"]:
                    DEF = char["DEF"]
                    typing("Your defence went up to "+str(DEF))
            elif Battle_choice == "3":
                if inventory["ATKpotion"] > 0:
                    ATK += round(0.5*ATK)
                    typing("You gain " + str(ATK - char["ATK"]) + " attack for the rest of this battle")
                    Battle_choice = 0
                else:
                    clrscrn()
                    print("Out of attack potions")
                    time.sleep(1)
                    clrscrn()
                    Battle_choice = 1
            elif Battle_choice == "4":
                if inventory["HPpotion"] > 0:
                    befor_potionHP = HP
                    HP += round(0.25*Hp)
                    if HP > char["HP"]:
                        HP = char["HP"]
                    typing("You gain " + str(HP - befor_potionHP) + " HP from the potion.")
                    Battle_choice = 0
                else:
                    clrscrn()
                    print("Out of HP potions")
                    time.sleep(1)
                    clrscrn()
                    Battle_choice = 1
        while ehp > 0 and HP >0:                                #this contains the enemy decision tree needs to be randomised a bit too
            print("Opponents turn")
            roundHP = HP
            time.sleep(1)
            if edef == 0:
                typing(epickname + " is defending.")
                edef += round(0.7 * epick["edef"])
            elif edef == epick["edef"] and ehp == epick["ehp"]:
                Typing(epickname + " attacks.")
                eatk += random.randint(-2,2)
                if DEF < eatk:
                    DEF -= eatk
                    HP += DEF
                elif DEF > eatk:
                    DEF -= eatk
                else: 
                    HP -= eatk
                if DEF < 0 :
                    DEF = 0
                    typing("The enemy broke through your defence.")
                print("You lost " + str(roundHP - HP)+" HP.")
                Battle_choice = 0
            #if def = 0 use defend
            #if hp and def == master amounts use atk

#enemy dictionary for the function to be defined
char = {'HP':10,'ATK':15,'DEF':5,'LVL':1,'XP':0,'LVLNEXT':10}

enemylist = {
    "Imp"    : {'ehp':10, 'eatk':4, 'edef':2, 'expgain':13},
    "Ogre"   : {'ehp':15, 'eatk':1, 'edef':12, 'expgain':13},
    "Dwarf"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Tiny Hands" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Giant"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Goblin" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Ghoul"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Psycho" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13}}

inventory = {'HPpotion':0, 'ATKpotion':10}

battle_sequence(enemylist,char,inventory)

#running the actual battles



"""
pick enemy

    get enemy stats                                  done
store to local variable                              done
alter stats to be balanced against player level      done

    get player stats                                 done char
store to a local variable                            

start fight

    pick who goes first
random intiger 1 is player 2 is enemy
        there may be a more efficient way of doing this like def player turn and def enemy turn and have an if function for the base of 1 0r 2 ro be platyer start or not 
        ie
        if var == 1:
            player turn()
            while ehp >=0 and hp >=0:
                enemy TURN()
                PLAYER TURN()

        make turn logger

        player turn
            choose action to make
             if attack perform effect changes to enemy hp
                player attack+random number -2/+2 *
             if status changer perform changes to player stats
        
        
        enemy turn
             if attack perform effect changes to enemy hp
             if status changer perform changes to player stats
"""