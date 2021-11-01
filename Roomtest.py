#this file is to test a room system
import os
import sys
import cmd
import random
import time

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00)

def clrscrn():
    if os.name == 'posix':
        _=os.system("clear")
    else:
        _=os.system('cls')

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
        char['ATK'] +=5
#increase base atk stat
        char['DEF'] +=5
#increase base def stat
        char['HP'] +=5
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
            
def endscr():        #endscreen for when you die
    clrscrn()
    
    
    redo = input ("Thank you for playing our game, If you would like to play again Press 1, Press 2 to exit\n")
    if redo == ("1"):
        title_screen()
    elif redo == ("2"):
        os.system(exit)

def enemy_pick(enemylist,char,boss):
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

    Starter_Dragon_String = '''

████████╗██╗░░██╗███████╗  ░██████╗████████╗░█████╗░██████╗░████████╗███████╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
░░░██║░░░███████║█████╗░░  ╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░█████╗░░██████╔╝
░░░██║░░░██╔══██║██╔══╝░░  ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║███████╗  ██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

██████╗░██████╗░░█████╗░░██████╗░░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║
██║░░██║██████╔╝███████║██║░░██╗░██║░░██║██╔██╗██║
██║░░██║██╔══██╗██╔══██║██║░░╚██╗██║░░██║██║╚████║
██████╔╝██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░╚███║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚══╝

'''
    if boss["boss_room"] == 1:
        epickname = "The Starter Dragon"
        estring = Starter_Dragon_String
        print(estring)
        epick = boss
        print("\n")
        typing("It stands ahead, the cause and reason for your dungeon delving.\nThe beast which has plagued your people for generations.\nThe alabaster horror. The starter.")
        time.sleep(3)    
    else:

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

def battle_sequence(enemylist,char,inventory,boss):

#choose the random enemy and set their
    enemy_pick(enemylist,char,boss)

#define local variables for the player stats to be used here for ease
    HP = char["HP"]
    ATK = char["ATK"]
    DEF = char["DEF"]

    global ehp
    global eatk
    global edef
    global expgain
    global emhp
    global emdef

    ehp = epick["ehp"]
    eatk = epick["eatk"]
    edef = epick["edef"]
    expgain = epick["expgain"]
    emhp = epick["ehp"]
    emdef = epick["edef"]

    if boss["boss_room"] != 1:
        ehp *= round((char["HP"]+char["DEF"]+char["ATK"])/3)
        eatk *= round((char["HP"]+char["DEF"]+char["ATK"])/3)
        edef *= round((char["HP"]+char["DEF"]+char["ATK"])/3)
        emhp *= round((char["HP"]+char["DEF"]+char["ATK"])/3)
        edef *= round((char["HP"]+char["DEF"]+char["ATK"])/3)

        ehp = int(ehp)
        eatk = int(eatk)
        edef =  int(edef)
        emhp = int(emhp)
        edef = int(edef)
        ematk = eatk

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
            print("Player Armor:    " + str(DEF) + "/" + str(char["DEF"])+"\n")
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
            print("Player Armor:    " + str(DEF) + "/" + str(char["DEF"])+"\n\n")
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
                    eatk = ematk
                else:
#enemy defense function
                    typing(epickname + " is defending!"+"\n")
                    edef += round(0.7 * emdef)
                    if edef > emdef:
                        edef = emdef
            else:
#enemy defense function
                if edef == 0 and HP > eatk-5:
                    typing(epickname + " is defending!"+"\n")
                    edef += round(0.7 * emdef)
                    if edef > emdef:
                        edef = emdef
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
                    eatk = ematk
            time.sleep(2)
            Battle_choice = 5
            
            if HP > 0 :
#players turn in While loop *************************************************************************************************************************************************
                while Battle_choice != 0: 
                    clrscrn()
                    print(estring)
                    print("Enemy HP:        " + str(ehp) + "/" + str(emhp))
                    print("\nPlayer HP:       " + str(HP) + "/" + str(char["HP"]))
                    print("Player Armor:    " + str(DEF) + "/" + str(char["DEF"])+ "\n")
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
            typing ("You have been slain by " + epickname + ".\nSomeone else will have to finish your quest, or maybe Dewi will complete it alone.")
            time.sleep(2)
            clrscrn()
            #endscr()

def room1(inventory):
#the lair
    clrscrn()
    global room
    global room_string
    room = 1
    room_string = '''
    █████████████████████████████████████████
    █─▄─▄─█─█─█▄─▄▄─███▄─▄████▀▄─██▄─▄█▄─▄▄▀█
    ███─███─▄─██─▄█▀████─██▀██─▀─███─███─▄─▄█
    ▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▀▄▄▀
    '''
    print(room_string)
    
    typing("\nYou enter the lair of the beast.")
    time.sleep(0.3)
    typing("\nA long corridor leads you to a square chamber shrouded in darnkness which resembles a shrine for some deity.")
    time.sleep(0.3)
    typing("\nThe smell of sulfur and old blood fills your sinuses and slightly blurs your vision. ")
    time.sleep(0.3)
    typing("\nThe creaking ground under your feet holds steady as you tread with care through the area. ")
    time.sleep(0.3)
    typing("\nSearching the chamber you find a sconce and using a tinderbox you light a small fire lighting up this space.  ")   
    time.sleep(2)
    typing("\nAs you turn you see it.")
    time.sleep(2)
    clrscrn()

    battle_sequence(enemylist,char,inventory,boss)

    print ("congratulations you have defeted the " +str(epickname) +" in its lair")

    item_find = random.randint(0,2)
    if item_find == 1:
        typing("You found a health potion on the fallen "+str(epickname)+"\n")
        inventory["HPpotion"] += 1
    elif item_find == 2:
        typing("You found a attack potion on the fallen "+str(epickname)+"\n")
        inventory["ATKpotion"] += 1
        
    mvnt = input("to your East there is a big black door, its open.\nTo your West there is a dark corridor, which way will you go?\n(Type E or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "E" or mvnt == "e":
            room3(inventory)
        elif mvnt == "W" or mvnt == "w":
            room2(inventory)
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("W") or mvnt !=  ("w"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    clrscrn()
 
def room2(inventory):
#the cavern
    clrscrn()
    global room
    global room_string
    room = 1
    room_string = '''
    █████████████████████████████████████████████████████████
    █─▄─▄─█─█─█▄─▄▄─███─▄▄▄─██▀▄─██▄─█─▄█▄─▄▄─█▄─▄▄▀█▄─▀█▄─▄█
    ███─███─▄─██─▄█▀███─███▀██─▀─███▄▀▄███─▄█▀██─▄─▄██─█▄▀─██
    ▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀
    '''
    print(room_string)

    typing("\nDarkness prevails over light here in the cavern.")
    time.sleep(0.3)
    typing("\nStalagmites hang low offering sharp obstacles to traverse in this desolate cave with their counterpart stalactites jutting from the land.")
    time.sleep(0.3)
    typing("\nVoids and crevices dot the floor in uneven patterns giving access to insects, arachnids and small rodents between the caves chambers.")
    time.sleep(0.3)
    typing("\nTravel through this area leads you through a crawlspace to a small cavern where small tunnels lead out in other directions.")
    time.sleep(0.3)
    typing("\nA large hole in the floor gazes down into the darkness bellow.")   
    time.sleep(2)
    typing("\nNoise emanates from bellow before something emerges.")
    time.sleep(2)
    clrscrn()

    battle_sequence(enemylist,char,inventory,boss)
    print ("congratulations you have defeted the " +str(epickname) +" under the caverns.")
    
    item_find = random.randint(0,2)
    if item_find == 1:
        typing("You found a health potion on the fallen "+str(epickname)+"\n")
        inventory["HPpotion"] += 1
    elif item_find == 2:
        typing("You found a attack potion on the fallen "+str(epickname)+"\n")
        inventory["ATKpotion"] += 1
        
    mvnt = input("(Type S or E to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "S" or mvnt == "s":
            room4(inventory)
        elif mvnt == "E" or mvnt == "e":
            room1(inventory)
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("S") or mvnt !=  ("s"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    
def room3(inventory):
#the Grotto
    clrscrn()
    global room
    global room_string
    room = 1
    room_string = '''
    ███████████████████████▀█████████████████████████████
    █─▄─▄─█─█─█▄─▄▄─███─▄▄▄▄█▄─▄▄▀█─▄▄─█─▄─▄─█─▄─▄─█─▄▄─█
    ███─███─▄─██─▄█▀███─██▄─██─▄─▄█─██─███─█████─███─██─█
    ▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▀
    '''
    print(room_string)

    typing("\nThe first thing that hits you is the humidity, the warm damp air drawn through this tunnel.")
    time.sleep(0.3)
    typing("\nGreenery grows here in the underground, possibly a food source for the denizens of this place.")
    time.sleep(0.3)
    typing("\nMoss covered rocks and deep plant life wrap the ground and walls ubiquitously.")
    time.sleep(0.3)
    typing("\nA thin bead of sunlight stems from a fissure in the grottos ceiling, the cause of this underground natural balance.")
    time.sleep(0.3)
    typing("\nThe slippery surface makes travel difficult here and even though the ray  of light give a semblance of freedom the spaces closeness still pushes on you.")   
    time.sleep(2)
    typing("\nSuddenly a blanket of moss from a near wall falls away revealing it.")
    time.sleep(2)
    clrscrn()

    battle_sequence(enemylist,char,inventory,boss)
    print ("congratulations you have defeted the " +str(epickname) +" inside the grotto.")

    item_find = random.randint(0,2)
    if item_find == 1:
        typing("You found a health potion on the fallen "+str(epickname)+"\n")
        inventory["HPpotion"] += 1
    elif item_find == 2:
        typing("You found a attack potion on the fallen "+str(epickname)+"\n")
        inventory["ATKpotion"] += 1
        
    mvnt = input("(Type S or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "S" or mvnt == "s":
            room5(inventory)
        elif mvnt == "W" or mvnt == "w":
            room1(inventory)
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("S") or mvnt !=  ("s"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    
def room4(inventory):
#the gorge
    clrscrn()
    global room
    global room_string
    room = 1
    room_string = '''
    ███████████████████████▀████████████████▀███████
    █─▄─▄─█─█─█▄─▄▄─███─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█▄─▄▄─█
    ███─███─▄─██─▄█▀███─██▄─█─██─██─▄─▄█─██▄─██─▄█▀█
    ▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    '''
    print(room_string)

    typing("\nA smooth stone chamber and winding tunnels intersect from here heading into water between your knees and neck deep.")
    time.sleep(0.3)
    typing("\nHeading up from here you find yourself standing thirty meters above the water in a circular space where three natural stone bridges cross the water on differing levels.")
    time.sleep(0.3)
    typing("\nHigher and higher you climb following the trail, still dripping wet from being in the water below.")
    time.sleep(0.3)
    typing("\nRounding a bend past the highest of the bridges you stumble across a much deeper cut in the land.")
    time.sleep(0.3)
    typing("\nA cavern deeper that you can see is before you with another natural bridge crossing it close to the ceiling.")   
    time.sleep(2)
    typing("\nAs you begin to cross a sound catches you from behind.")
    time.sleep(2)
    clrscrn()

    battle_sequence(enemylist,char,inventory,boss)  
    print ("congratulations you have defeted the " +str(epickname) +" in the gorge.")

    item_find = random.randint(0,2)
    if item_find == 1:
        typing("You found a health potion on the fallen "+str(epickname)+"\n")
        inventory["HPpotion"] += 1
    elif item_find == 2:
        typing("You found a attack potion on the fallen "+str(epickname)+"\n")
        inventory["ATKpotion"] += 1
        
    mvnt = input("(Type N or E to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            room2(inventory)
        elif mvnt == "E" or mvnt == "e":
            room6(inventory)
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("N") or mvnt !=  ("n"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()

def room5(inventory):
#the Tomb
    clrscrn()
    global room
    global room_string
    room = 1
    room_string = '''
    ████████████████████████████████████████████
    █─▄─▄─█─█─█▄─▄▄─███─▄─▄─█─▄▄─█▄─▀█▀─▄█▄─▄─▀█
    ███─███─▄─██─▄█▀█████─███─██─██─█▄█─███─▄─▀█
    ▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀
    '''
    print(room_string)

    typing("\nOnce again you are in total darkness.")
    time.sleep(0.3)
    typing("\nFeeling the walls as you move you figure yourself to be within some cut stone chamber.")
    time.sleep(0.3)
    typing("\nA cool but damp air draughts throughout the space bringing with it the smell of decay.")
    time.sleep(0.3)
    typing("\nLighting a torch you see nearby you a number of stonework coffins become visible, you are within a place of rest.")
    time.sleep(0.3)
    typing("\nA cracking sound originates from one of the stone caskets as the lid drops to the floor.")   
    time.sleep(2)
    typing("\nNext to the container you see it.")
    time.sleep(2)
    clrscrn()

    battle_sequence(enemylist,char,inventory,boss)
    print ("congratulations you have defeted the " +str(epickname) +" in the tomb.")

    item_find = random.randint(0,2)
    if item_find == 1:
        typing("You found a health potion on the fallen "+str(epickname)+"\n")
        inventory["HPpotion"] += 1
    elif item_find == 2:
        typing("You found a attack potion on the fallen "+str(epickname)+"\n")
        inventory["ATKpotion"] += 1

    mvnt = input("(Type N or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            room3(inventory)
        elif mvnt == "W" or mvnt == "w":
            room6(inventory)
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("N") or mvnt !=  ("n"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    clrscrn()

def room6(inventory):
#the scorched chambers
    clrscrn()
    global room
    global room_string
    room = 1
    room_string = '''
    ████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █─▄─▄─█─█─█▄─▄▄─███─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄▀█─▄▄▄─█─█─█▄─▄▄─█▄─▄▄▀███─▄▄▄─█─█─██▀▄─██▄─▀█▀─▄█▄─▄─▀█▄─▄▄─█▄─▄▄▀█
    ███─███─▄─██─▄█▀███▄▄▄▄─█─███▀█─██─██─▄─▄█─███▀█─▄─██─▄█▀██─██─███─███▀█─▄─██─▀─███─█▄█─███─▄─▀██─▄█▀██─▄─▄█
    ▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀
    '''
    print(room_string)

    typing("\nA thickness to the air fills your nose as a stuffy burnt aroma begins to overwhelm you.")
    time.sleep(0.3)
    typing("\nA dimly lit chamber lies in ahead with walls and ceiling coated in a fine black powder.")
    time.sleep(0.3)
    typing("\nSoot! Soot is coating this chamber, a thick coating from something burning.")
    time.sleep(0.3)
    typing("\nBut what has been burning.")
    time.sleep(0.3)
    typing("\nA crash behind you forces you to start and turn.")   
    time.sleep(2)
    typing("\nIn the shadows of soot it appears.")
    time.sleep(2)
    clrscrn()

    battle_sequence(enemylist,char,inventory,boss)
    print ("congratulations you have defeted the " +str(epickname) +" within the scorched chamber.")

    item_find = random.randint(0,2)
    if item_find == 1:
        typing("You found a health potion on the fallen "+str(epickname)+"\n")
        inventory["HPpotion"] += 1
    elif item_find == 2:
        typing("You found a attack potion on the fallen "+str(epickname)+"\n")
        inventory["ATKpotion"] += 1

    mvnt = input("(THE BOSS ROOM IS TO THE NORTH Type W or E OR N to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            bossroom()
        elif mvnt == "W" or mvnt == "w":
            room4(inventory)
        elif mvnt == "E" or mvnt == "e":
            room5(inventory)
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("N") or mvnt != ("n") or mvnt != ("E") or mvnt !=  ("e"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
   
def bossroom():

    clrscrn()
    print ("THIS IS THE BOSS BITCH") #tell the player which room they are in    
    time.sleep(2)
    clrscrn()
    time.sleep(2)
    boss['boss_room'] = 1
    battle_sequence(enemylist,char,inventory,boss)
    clrscrn()
    time.sleep(2)
    typing("You did it……..?\nHonestly I didn’t expect you to get this far.\nThis was supposed to be beatable but the time needed to get to a level to beat this guy was silly.\nAre you okay? Can I get you some water or something?\nWell anyway, you have completed your quest.\nThe Starter Dragon has fallen and you can return home knowing that your people are safe.\n...................................")
    time.sleep(5)
    typing("\nFor Now")
    time.sleep(5)
    clrscrn()
    typing("We look forward to seeing you in v.2")
    time.sleep(2)
    endscr()

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

#inventory dictionary
inventory = {'HPpotion':2, 'ATKpotion':2}

#dict for the boss
boss = {'ehp':150, 'eatk':150, 'edef':150, 'expgain':9001,'boss_room':0}

