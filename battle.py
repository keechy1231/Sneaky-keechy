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
    global estring

    epickname = enemypick[0]
    epick = dict(enemypick[1])

#epickname shows the chosen enemys name
#epick is the chosen enemys stats as a dictionary

#ascii text generator to change if needed https://patorjk.com/software/taag/#p=display&f=Big%20Chief&t=Tiny%20Hands
    Imp_string = '''

████████╗██╗░░██╗███████╗  ██╗███╗░░░███╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ██║████╗░████║██╔══██╗
░░░██║░░░███████║█████╗░░  ██║██╔████╔██║██████╔╝
░░░██║░░░██╔══██║██╔══╝░░  ██║██║╚██╔╝██║██╔═══╝░
░░░██║░░░██║░░██║███████╗  ██║██║░╚═╝░██║██║░░░░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░

'''

    Ogre_string = '''

████████╗██╗░░██╗███████╗  ░█████╗░░██████╗░██████╗░███████╗
╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔════╝░██╔══██╗██╔════╝
░░░██║░░░███████║█████╗░░  ██║░░██║██║░░██╗░██████╔╝█████╗░░
░░░██║░░░██╔══██║██╔══╝░░  ██║░░██║██║░░╚██╗██╔══██╗██╔══╝░░
░░░██║░░░██║░░██║███████╗  ╚█████╔╝╚██████╔╝██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝

'''

    Dwarf_string = '''

████████╗██╗░░██╗███████╗  ██████╗░░██╗░░░░░░░██╗░█████╗░██████╗░███████╗
╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝
░░░██║░░░███████║█████╗░░  ██║░░██║░╚██╗████╗██╔╝███████║██████╔╝█████╗░░
░░░██║░░░██╔══██║██╔══╝░░  ██║░░██║░░████╔═████║░██╔══██║██╔══██╗██╔══╝░░
░░░██║░░░██║░░██║███████╗  ██████╔╝░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██║░░░░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░
                                                           
'''

    Bird_string = '''

████████╗██╗███╗░░██╗██╗░░░██╗  ██╗░░██╗░█████╗░███╗░░██╗██████╗░░██████╗
╚══██╔══╝██║████╗░██║╚██╗░██╔╝  ██║░░██║██╔══██╗████╗░██║██╔══██╗██╔════╝
░░░██║░░░██║██╔██╗██║░╚████╔╝░  ███████║███████║██╔██╗██║██║░░██║╚█████╗░
░░░██║░░░██║██║╚████║░░╚██╔╝░░  ██╔══██║██╔══██║██║╚████║██║░░██║░╚═══██╗
░░░██║░░░██║██║░╚███║░░░██║░░░  ██║░░██║██║░░██║██║░╚███║██████╔╝██████╔╝
░░░╚═╝░░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═════╝░

'''

    Giant_string ='''

████████╗██╗░░██╗███████╗  ░██████╗░██╗░█████╗░███╗░░██╗████████╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝░██║██╔══██╗████╗░██║╚══██╔══╝
░░░██║░░░███████║█████╗░░  ██║░░██╗░██║███████║██╔██╗██║░░░██║░░░
░░░██║░░░██╔══██║██╔══╝░░  ██║░░╚██╗██║██╔══██║██║╚████║░░░██║░░░
░░░██║░░░██║░░██║███████╗  ╚██████╔╝██║██║░░██║██║░╚███║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░
                                                      
'''

    Goblin_string = '''

████████╗██╗░░██╗███████╗  ░██████╗░░█████╗░██████╗░██╗░░░░░██╗███╗░░██╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝░██╔══██╗██╔══██╗██║░░░░░██║████╗░██║
░░░██║░░░███████║█████╗░░  ██║░░██╗░██║░░██║██████╦╝██║░░░░░██║██╔██╗██║
░░░██║░░░██╔══██║██╔══╝░░  ██║░░╚██╗██║░░██║██╔══██╗██║░░░░░██║██║╚████║
░░░██║░░░██║░░██║███████╗  ╚██████╔╝╚█████╔╝██████╦╝███████╗██║██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═╝╚═╝░░╚══╝
                                                          
'''

    Ghoul_string = '''

████████╗██╗░░██╗███████╗  ░██████╗░██╗░░██╗░█████╗░██╗░░░██╗██╗░░░░░
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝░██║░░██║██╔══██╗██║░░░██║██║░░░░░
░░░██║░░░███████║█████╗░░  ██║░░██╗░███████║██║░░██║██║░░░██║██║░░░░░
░░░██║░░░██╔══██║██╔══╝░░  ██║░░╚██╗██╔══██║██║░░██║██║░░░██║██║░░░░░
░░░██║░░░██║░░██║███████╗  ╚██████╔╝██║░░██║╚█████╔╝╚██████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝
                                                     
'''

    Psycho_string = '''

████████╗██╗░░██╗███████╗  ██████╗░░██████╗██╗░░░██╗░█████╗░██╗░░██╗░█████╗░
╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔════╝╚██╗░██╔╝██╔══██╗██║░░██║██╔══██╗
░░░██║░░░███████║█████╗░░  ██████╔╝╚█████╗░░╚████╔╝░██║░░╚═╝███████║██║░░██║
░░░██║░░░██╔══██║██╔══╝░░  ██╔═══╝░░╚═══██╗░░╚██╔╝░░██║░░██╗██╔══██║██║░░██║
░░░██║░░░██║░░██║███████╗  ██║░░░░░██████╔╝░░░██║░░░╚█████╔╝██║░░██║╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░╚════╝░

'''


    if epickname == "Imp":
        estring = Imp_string
        print(estring)
        print("\n")
        typing("A small winged demon crouches in front of you.\nIts sharp teeth gnarled and stained from devouring meat and bones.\nThe creature bounds back as it sees you then leaps!")
        time.sleep(3)

    elif epickname == "Ogre":
        estring = Ogre_string
        print(estring)
        print("\n")
        typing("A mammoth of a humanoid stands stooped in front of you.\nTheir head scraping on the ceiling as it mulls around its lair.\nIt looks at you and after a few seconds of pondering begins at you!")
        time.sleep(3)

    elif epickname == "Dwarf":
        estring = Dwarf_string
        print(estring)
        print("\n")
        typing("A stout, short man stumbles ahead of you.\nStains on his long beard and alcohol on his breath he stares at the doorway you stand in.\nHe raises his axe and charges!")
        time.sleep(3)

    elif epickname == "Tiny Hands":
        estring = Bird_string
        print(estring)
        print("\n")
        typing("An elongated frame hunches over a bench.\nHolding out a ladle with a mushroom in, their grin widens to a full toothed maw.\nA cleaver is lifted and he begins to advance!")
        time.sleep(3)

    elif epickname == "Giant":
        estring = Giant_string
        print(estring)
        print("\n")
        typing("Crawling in this chamber lies a giant.\nIts form too large to even stand its bloodied knees scraped and calloused from the hard stone.\nHis reaching hand scratch towards your direction!")
        time.sleep(3)

    elif epickname == "Goblin":
        estring = Goblin_string
        print(estring)
        print("\n")
        typing("It’s a goblin.........really?\nSo there are giants and Demons but we give him a goblin to fight?\nOkay then, here’s a goblin.......")
        time.sleep(3)

    elif epickname == "Ghoul":
        estring = Ghoul_string
        print(estring)
        print("\n")
        typing("A ghastly figure floats ahead.\nIts hollow form and featureless face stressed in a painful simulation.\nlifting its hand the air converts to an iced consistency!")
        time.sleep(3)

    elif epickname == "Psycho":
        estring = Psycho_string
        print(estring)
        print("\n")
        typing("A woman lounges in a chair in the leading chamber.\nClutching a hatchet coated in blood she screams at your sight.\nflinging the chair behind her she manically sprints for you!")
        time.sleep(3)

def level(char,): 
#Level system for the hero
       while char['XP'] >= char['LVLNEXT']: 
#if xp is greater to or equal to lvlnext xp then go through the below commands
        char['LVL'] += 1 
#level will go up by 1
        char['XP'] = char['XP'] - char['LVLNEXT'] 
#take xp away from lvlnext to get new xp value
        char['LVLNEXT'] = round(char['LVLNEXT'] * 1.2) 
#make lvlnext xp increase as the char levels up
        char['ATK'] += 1 
#increase base atk stat
        char['DEF'] += 1 
#increase base def stat
        char['HP'] +=1 
#increase base HP stat
        if char["XP"] < char["LVLNEXT"]: 
#once the char can level no more output the below to show new stats. 
            typing("Congratulations you have reached level " + str(char["LVL"]) + "\n")
            time.sleep(0.1)
            print("\nCurrent XP             " + str(char["XP"]))
            time.sleep(0.1)
            print("XP to next level       " + str(char["LVLNEXT"]))
            time.sleep(0.1)
            print("HP                   ^ " + str(char["HP"]))
            time.sleep(0.1)
            print("Attack               ^ " + str(char["ATK"]))
            time.sleep(0.1)
            print("Defense              ^ " + str(char["DEF"]))

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
    emhp = epick["ehp"]

    ehp *= char["LVL"]
    eatk *= char["LVL"]
    edef *= char["LVL"]
    expgain *= char["LVL"]
    emhp *= char["LVL"]


#making a round counter for the battle not used fully yet
    Battle_round = 0

#pick weather the player or opponant will go first on 1 the player will go first
    battle_start_modifier = 0  #random.randint(0,1)

#battle choice is the loop controaler. 1 is replay, 0 is next step
   
    Battle_choice = 5
    if battle_start_modifier == 0:
        typing("\nYou got the jump on your opponent!\n\n")
        time.sleep(2)
#player round 1 attack ***********************************************************************************************************************************************************************
        while Battle_choice != 0:
            clrscrn()
            roundehp = ehp
#print the battle state
            print(estring)
            print("Enemy HP:        " + str(ehp) + "/" + str(emhp))
            print("\nPlayer HP:       " + str(HP) + "/" + str(char["HP"]))
            print("Player Armor:   " + str(DEF) + "/" + str(char["DEF"])+"\n")
            print("\nPLAYERS TURN\n")

            print("Choose your action:")
            print("1 Attack         " + str(ATK))
            print("2 Defend         " + str(DEF))
            print("3 Attack Potion  " + str(inventory["ATKpotion"])+ " avaliable")
            print("4 Health Potion  " + str(inventory["HPpotion"])+ " avaliable\n\n")
            Battle_choice = input()
#attack action, take damage away from defense then add defense
            if Battle_choice == "1":
                ATK += random.randint(-2,2)
                if edef < ATK and edef != 0:
                    edef -= ATK
                    ehp += edef
                    typing("The Enemy lost " + str(roundehp - ehp)+" HP.\n")
                elif edef >= ATK:
                    edef -= ATK
                    typing("Your attack was blocked.\n")
                else: 
                    ehp -= ATK
                    typing("The Enemy lost " + str(roundehp - ehp)+" HP.\n")
                if edef < 0 :
                    edef = 0
                    typing("You broke through your opponents armor\n")
                ATK = char["ATK"]
                Battle_choice = 0
#Defense action calculater
            elif Battle_choice == "2":
                DEF += round(0.7 * char["DEF"])
                Battle_choice = 0
                if DEF > char["DEF"]:
                    DEF = char["DEF"]
                    typing("Your defence went up to "+str(DEF)+"\n")
#take an attack potion stackable
            elif Battle_choice == "3":
                if inventory["ATKpotion"] > 0:
                    ATK += round(0.5*ATK)
                    typing("You gain " + str(ATK - char["ATK"]) + " attack for the rest of this battle\n")
                    inventory["ATKpotion"] -=1
                    Battle_choice = 0
                else:
                    clrscrn()
                    typing("Out of attack potions"+"\n")
                    time.sleep(1)
                    clrscrn()
                    Battle_choice = 5
#take a hp potion
            elif Battle_choice == "4":
                if HP == char["HP"]:
                    typing("You are already at max health"+"\n")
                    Battle_choice = 5
                    clrscrn()
                else:
                    if inventory["HPpotion"] > 0:
                        befor_potionHP = HP
                        HP += round(0.8*char["HP"])
                        if HP > char["HP"]:
                            HP = char["HP"]
                        typing("You gain " + str(HP - befor_potionHP) + " HP from the potion."+"\n")
                        inventory["HPpotion"] -=1
                        Battle_choice = 0
                    else:
                        clrscrn()
                        typing("Out of HP potions"+"\n")
                        time.sleep(1)
                        clrscrn()
                        Battle_choice = 5
            else:
                Battle_choice = 5
        time.sleep(2)
        
    if 0 == 0:
#this only runs if the randomiser calls for opponent to go first
        if battle_start_modifier == 1:
            typing("\nYour Opponent got the jump on you!\n\n")
            time.sleep(2)
        while ehp > 0 and HP >0:                                
#enemy turn in while function ***********************************************************************************************************************************************************
            Battle_round += 1
            Battle_choice = 5
            clrscrn()
            roundehp = ehp
            roundHP = HP
            print(estring)
            print("Enemy HP:        " + str(ehp) + "/" + str(emhp))
            print("\nPlayer HP:       " + str(HP) + "/" + str(char["HP"]))
            print("Player Armor:   " + str(DEF) + "/" + str(char["DEF"])+"\n\n")
            print("OPPONENTS TURN\n")
            time.sleep(1)
            opponent_randomiser1 = random.randint(0,1)
            if opponent_randomiser1 == 0:
                opponent_randomiser2 = random.randint(0,1)
                if opponent_randomiser2 == 0:
#enemy attack function
                    typing(epickname + " is attacking!\n")                 
                    eatk += random.randint(-2,2)
                    if DEF < eatk and DEF != 0:
                        DEF -= eatk
                        HP += DEF
                        typing("You lost " + str(roundHP - HP)+" HP.\n")
                    elif DEF >= eatk:
                        DEF -= eatk
                        typing("You blocked their attack.\n")
                    else: 
                        HP -= eatk
                        typing("You lost " + str(roundHP - HP)+" HP.\n")
                    if DEF < 0 :
                        DEF = 0
                        typing("Your opponent broke through your armor\n")
                    eatk = epick["eatk"]
                else:
#enemy defense function
                    typing(epickname + " is defending!"+"\n")
                    edef += round(0.7 * epick["edef"])
                    if edef > epick["edef"]:
                        edef = epick["edef"]
            else:
#enemy defense function
                if edef == 0 and HP > eatk-5:
                    typing(epickname + " is defending!"+"\n")
                    edef += round(0.7 * epick["edef"])
                    if edef > epick["edef"]:
                        edef = epick["edef"]
                else:
#enemy attack function
                    typing(epickname + " is attacking!"+"\n")
                    eatk += random.randint(-2,2)
                    if DEF < eatk and DEF != 0:
                        DEF -= eatk
                        HP += DEF
                        typing("You lost " + str(roundHP - HP)+" HP."+"\n")
                    elif DEF >= eatk:
                        DEF -= eatk
                        typing("You blocked their attack."+"\n")
                    else: 
                        HP -= eatk
                        typing("You lost " + str(roundHP - HP)+" HP."+"\n")
                    if DEF < 0 :
                        DEF = 0
                        typing("Your opponent broke through your armor"+"\n")
                    eatk = epick["eatk"]
            time.sleep(2)
            Battle_choice = 5
            
            if HP > 0 :
#players turn in While loop *************************************************************************************************************************************************
                while Battle_choice != 0: 
                    clrscrn()
                    print(estring)
                    print("Enemy HP:        " + str(ehp) + "/" + str(emhp))
                    print("\nPlayer HP:       " + str(HP) + "/" + str(char["HP"]))
                    print("Player Armor:   " + str(DEF) + "/" + str(char["DEF"])+ "\n")
                    print("\nPLAYERS TURN\n")
                    print("\nChoose your action:")
                    print("1 Attack         " + str(ATK))
                    print("2 Defend         " + str(DEF))
                    print("3 Attack Potion  " + str(inventory["ATKpotion"])+ " avaliable")
                    print("4 Health Potion  " + str(inventory["HPpotion"])+ " avaliable\n\n")
                    Battle_choice = input()
#attack action, take damage away from defense then add defense
                    if Battle_choice == "1":
                        ATK += random.randint(-2,2)
                        if edef < ATK and edef != 0:
                            edef -= ATK
                            ehp += edef
                            typing("The Enemy lost " + str(roundehp - ehp)+" HP."+"\n")
                        elif edef >= ATK:
                            edef -= ATK
                            typing("Your attack was blocked.\n")
                        else: 
                            ehp -= ATK
                            typing("The Enemy lost " + str(roundehp - ehp)+" HP."+"\n")
                        if edef < 0 :
                           edef = 0
                           typing("You broke through your opponents armor\n")
                        ATK = char["ATK"]
                        Battle_choice = 0
                        time.sleep(2)
#Defense calculater
                    elif Battle_choice == "2":
                        DEF += round(0.7 * char["DEF"])
                        Battle_choice = 0
                        if DEF > char["DEF"]:
                            DEF = char["DEF"]
                        typing("Your defence went up to "+str(DEF))
                        time.sleep(2)
#take an attack potion stackable
                    elif Battle_choice == "3":
                        if inventory["ATKpotion"] > 0:
                            ATK += round(0.5*ATK)
                            typing("You gain " + str(ATK - char["ATK"]) + " attack for the rest of this battle\n")
                            inventory["ATKpotion"] -=1
                            Battle_choice = 0
                            time.sleep(2)
                        else:
                            clrscrn()
                            typing("Out of attack potions"+"\n")
                            time.sleep(1)
                            clrscrn()
                            Battle_choice = 5
#take a hp potion
                    elif Battle_choice == "4":
                        if HP == char["HP"]:
                            typing("You are already at max health"+"\n")
                            Battle_choice = 5
                            clrscrn()
                        else:
                            if inventory["HPpotion"] > 0:
                                befor_potionHP = HP
                                HP += round(0.8*char["HP"])
                                if HP > char["HP"]:
                                    HP = char["HP"]
                                typing("You gain " + str(HP - befor_potionHP) + " HP from the potion."+"\n")
                                inventory["HPpotion"] -=1
                                Battle_choice = 0
                                time.sleep(2)
                            else:
                                typing("Out of HP potions"+"\n")
                                time.sleep(1)
                                clrscrn()


#battle should be finished if the code reaches this comment

        if HP > 0:
            clrscrn()
            typing("You have prevailed in this battle!\n")
            time.sleep(1)
            win = 1
            char['XP'] += expgain
            level(char)
        else:
            clrscrn()
            typing("You have died"+"\n")



#charecter
char = {'HP':10,'ATK':10,'DEF':10,'LVL':1,'XP':0,'LVLNEXT':10}

#enemy dictionary for the function to be defined
enemylist = {
    "Imp"    : {'ehp':1.1, 'eatk':0.7, 'edef':0.8, 'expgain':10},
    "Ogre"   : {'ehp':1.1, 'eatk':0.7, 'edef':0.8, 'expgain':13},
    "Dwarf"  : {'ehp':1.1, 'eatk':0.7, 'edef':0.8, 'expgain':13},
    "Tiny Hands" : {'ehp':1.3, 'eatk':1.3, 'edef':1.3, 'expgain':13},
    "Giant"  : {'ehp':1.1, 'eatk':0.7, 'edef':0.8, 'expgain':13},
    "Goblin" : {'ehp':1.1, 'eatk':0.7, 'edef':0.8, 'expgain':13},
    "Ghoul"  : {'ehp':1.1, 'eatk':0.7, 'edef':0.8, 'expgain':13},
    "Psycho" : {'ehp':1.1, 'eatk':0.7, 'edef':0.8, 'expgain':13}}

#dict for the boss
boss = {'bhp':150, 'batk':150, 'bdef':150 'expgain':9001}


#inventory dictionary
inventory = {'HPpotion':10, 'ATKpotion':10}

battle_sequence(enemylist,char,inventory)

input()
#running the actual battles



