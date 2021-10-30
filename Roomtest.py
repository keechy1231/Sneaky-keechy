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
        time.sleep(0.05)

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
        char['ATK'] += 1 
#increase base atk stat
        char['DEF'] += 1 
#increase base def stat
        char['HP'] +=1 
#increase base HP stat
        if char["XP"] < char["LVLNEXT"]: 
#once the char can level no more output the below to show new stats. 
            typing("Congratulations you have reached level " + str(char["LVL"]) + "\n")
            time.sleep(1)
            print("\nCurrent XP             " + str(char["XP"]))
            print("XP to next level       " + str(char["LVLNEXT"]))
            print("HP                   ^ " + str(char["HP"]))
            print("Attack               ^ " + str(char["ATK"]))
            print("Defense              ^ " + str(char["DEF"]))

#charecter
char = {'HP':2,'ATK':20,'DEF':0,'LVL':1,'XP':0,'LVLNEXT':10}

#enemy dictionary for the function to be defined
enemylist = {
    "Imp"    : {'ehp':10, 'eatk':4, 'edef':2, 'expgain':13},
    "Ogre"   : {'ehp':15, 'eatk':11, 'edef':12, 'expgain':13},
    "Dwarf"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Tiny Hands" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Giant"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Goblin" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Ghoul"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Psycho" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13}}

#inventory dictionary
inventory = {'HPpotion':10, 'ATKpotion':10}

def endscr():        #endscreen for when you die
    clrscrn()
    
    
    redo = input ("Thank you for playing our game, If you would like to play again Press 1, Press 2 to exit\n")
    if redo == ("1"):
        title_screen()
    elif redo == ("2"):
        os.system(exit)

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
        print(Imp_string)
        print("\n")
        typing("A small winged deamon crouches infront of you.\nIts sharp teeth gnarled and stained from devouring meat ans bones.\nThe creature bounds back as it sees you then leaps!")
        time.sleep(3)
    elif epickname == "Ogre":
        print(Ogre_string)
        print("\n")
        typing("A mammoth of a humanoid stands stooped infront of you./ Their head scraping on th ceiling as it mulls around its lair./n It looks at you and after a few seconds of pondering begins at you!")
        time.sleep(3)
    elif epickname == "Dwarf":
        print(Dwarf_string)
        print("\n")
        typing("A stout, short man stumbles ahead of you.\nStains on his long beard and alcahol on his breath he stares at the doorway you stand in.\nHe raises his axe and charges!")
        time.sleep(3)
    elif epickname == "Tiny Hands":
        print(Bird_string)
        print("\n")
        typing("An elongated frame hunches over a bench.\nHolding out a ladle with a mushroom in, their grin widens to a full toothed maw.\nA cleaver is lifted and he begins to advance!")
        time.sleep(3)
    elif epickname == "Giant":
        print(Giant_string)
        print("\n")
        typing("Crawling in this chanber lies a giant.\nIts form too large to even stand its bloodied knees scraped and calloused from the hard stone.\nHis reaching hand scratch towards your direction!")
        time.sleep(3)
    elif epickname == "Goblin":
        print(Goblin_string)
        print("\n")
        typing("Its a goblin.........really?\nSo there are giants and Deamons but we give him a gobline to fight?\nOkay then, heres a goblin.......")
        time.sleep(3)
    elif epickname == "Ghoul":
        print(Ghoul_string)
        print("\n")
        typing("A gastly figure floats ahead.\nIts hollow form and featureless face stressed in a painfull simulation.\nlifting its hand the air converts to an icey texture!")
        time.sleep(3)
    elif epickname == "Psycho":
        print(Psycho_string)
        print("\n")
        typing("A woman lounges in a chair in the leading chamber.\nClutching a hatchet coated in blood she screems at your sight.\nflighing the chair behind her she manicaly sprints for you!")
        time.sleep(3)
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

        if HP > 0:
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



def room1():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    battle_sequence(enemylist, char, inventory)
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("to your East there is a big black door, its open.  To your West there is a dark corridor, which way will you go? (Type E or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "E" or mvnt == "e":
            room3()
        elif mvnt == "W" or mvnt == "w":
            room2()
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("W") or mvnt !=  ("w"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    clrscrn()
 
 
def room2():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    battle_sequence(enemylist, char, inventory)
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(Type S or E to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "S" or mvnt == "s":
            room4()
        elif mvnt == "E" or mvnt == "e":
            room1()
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("S") or mvnt !=  ("s"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    


def room3():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    battle_sequence(enemylist, char, inventory)
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(Type S or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "S" or mvnt == "s":
            room5()
        elif mvnt == "W" or mvnt == "w":
            room1()
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("S") or mvnt !=  ("s"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    

def room4():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    battle_sequence(enemylist, char, inventory)
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(Type N or E to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            room2()
        elif mvnt == "E" or mvnt == "e":
            room6()
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("N") or mvnt !=  ("n"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()

def room5():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    battle_sequence(enemylist, char, inventory)
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(Type N or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            room3()
        elif mvnt == "W" or mvnt == "w":
            room6()
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("N") or mvnt !=  ("n"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    clrscrn()


def room6():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq(enemylist, char, inventory)  #goes to the death sequence function
        
    mvnt = input("(THE BOSS ROOM IS TO THE NORTH Type W or E OR N to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            bossroom()
        elif mvnt == "W" or mvnt == "w":
            room4()
        elif mvnt == "E" or mvnt == "e":
            room5()
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("N") or mvnt != ("n") or mvnt != ("E") or mvnt !=  ("e"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    

def bossroom():
    clrscrn()
    print ("THIS IS THE BOSS BITCH") #tell the player which room they are in    
    battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
room1()
