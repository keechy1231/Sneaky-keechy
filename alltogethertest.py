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
                    
#credits for when you die and or chose them at the begining        
def credits():
    clrscrn()
    print ("Created by;\nJason Mutter\nTomas Keech\n\nTwo Welsh idiots who have never met decided to make a python text game without any previous coding experience.\nWe hope you enjoyed our first iteration. There will be more!!\n\n\n\n")
    print ( '''
     :::    ::: :::::::::: :::::::::: ::::::::  :::    ::: :::   :::           :::     ::::    ::: :::::::::         ::::::::  ::::    ::: ::::::::::     :::     :::    ::: :::   ::: 
     :+:   :+:  :+:        :+:       :+:    :+: :+:    :+: :+:   :+:         :+: :+:   :+:+:   :+: :+:    :+:       :+:    :+: :+:+:   :+: :+:          :+: :+:   :+:   :+:  :+:   :+: 
     +:+  +:+   +:+        +:+       +:+        +:+    +:+  +:+ +:+         +:+   +:+  :+:+:+  +:+ +:+    +:+       +:+        :+:+:+  +:+ +:+         +:+   +:+  +:+  +:+    +:+ +:+  
     +#++:++    +#++:++#   +#++:++#  +#+        +#++:++#++   +#++:         +#++:++#++: +#+ +:+ +#+ +#+    +:+       +#++:++#++ +#+ +:+ +#+ +#++:++#   +#++:++#++: +#++:++      +#++:   
     +#+  +#+   +#+        +#+       +#+        +#+    +#+    +#+          +#+     +#+ +#+  +#+#+# +#+    +#+              +#+ +#+  +#+#+# +#+        +#+     +#+ +#+  +#+      +#+    
     #+#   #+#  #+#        #+#       #+#    #+# #+#    #+#    #+#          #+#     #+# #+#   #+#+# #+#    #+#       #+#    #+# #+#   #+#+# #+#        #+#     #+# #+#   #+#     #+#    
     ###    ### ########## ########## ########  ###    ###    ###          ###     ### ###    #### #########         ########  ###    #### ########## ###     ### ###    ###    ###    ''')
    back = input ("\n\n\n\n\n\n\nPress Enter to return to Title Screen, Or type exit to exit")
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

#clear screen function        
def clrscrn():
    if os.name == 'posix':
        _=os.system("clear")
    else:
        _=os.system('cls')
        
def start():
    clrscrn()
    time.sleep(3)        
    typing ("Welcome to The Starter.  A text based RPG made by two people who have no coding experience.\nIn this game you will choose from three classes to start your adventure.\nLevel up and become strong enough to take on the boss, you can fight as many enimies as you like before you fight the boss.  \n\n\n\n\n\n\n\n\n\n\nCreated by;\n\n")
    time.sleep(1)
    print ( '''
     :::    ::: :::::::::: :::::::::: ::::::::  :::    ::: :::   :::           :::     ::::    ::: :::::::::         ::::::::  ::::    ::: ::::::::::     :::     :::    ::: :::   ::: 
     :+:   :+:  :+:        :+:       :+:    :+: :+:    :+: :+:   :+:         :+: :+:   :+:+:   :+: :+:    :+:       :+:    :+: :+:+:   :+: :+:          :+: :+:   :+:   :+:  :+:   :+: 
     +:+  +:+   +:+        +:+       +:+        +:+    +:+  +:+ +:+         +:+   +:+  :+:+:+  +:+ +:+    +:+       +:+        :+:+:+  +:+ +:+         +:+   +:+  +:+  +:+    +:+ +:+  
     +#++:++    +#++:++#   +#++:++#  +#+        +#++:++#++   +#++:         +#++:++#++: +#+ +:+ +#+ +#+    +:+       +#++:++#++ +#+ +:+ +#+ +#++:++#   +#++:++#++: +#++:++      +#++:   
     +#+  +#+   +#+        +#+       +#+        +#+    +#+    +#+          +#+     +#+ +#+  +#+#+# +#+    +#+              +#+ +#+  +#+#+# +#+        +#+     +#+ +#+  +#+      +#+    
     #+#   #+#  #+#        #+#       #+#    #+# #+#    #+#    #+#          #+#     #+# #+#   #+#+# #+#    #+#       #+#    #+# #+#   #+#+# #+#        #+#     #+# #+#   #+#     #+#    
     ###    ### ########## ########## ########  ###    ###    ###          ###     ### ###    #### #########         ########  ###    #### ########## ###     ### ###    ###    ###    ''')            
    time.sleep(5)
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    #loop to get input needed to enter the game
    go = input("Please Press Enter to Begin\n")
    while 0 == 0 and go != 0:
        if go == ("") or go ==  (""):
                clrscrn()
                prologue(char)
        elif go != (""):
                typing ("Please Press Enter to Begin\n")
                go = 0
                go = input()

def title_screen_select():
    #loop to get the correct input from the title_screen so that the player cannot type anything and freeze the game
    option = input()
    while 0 == 0 and option != 0:
        if option == ("play") or option ==  ("Play"):
                start()
        elif option == ("Credits") or option ==  ("credits"):
                credits()
        elif option == ("Exit")or option == ("exit"):
                endscr()
        elif option != ("Play") or option != ("play") or option != ("Credits") or option !=  ("credits") or option != ("Exit") or option != ("exit"):
                typing ("please input valid command\n")
                option = 0
        option = input()
    
#the opeing screen of the game    
def title_screen():
    print (''' 
                                                                                    dMMP'
                                                                                    MMM:
                                                                                    YMMb.
                                                                                     YMMMb.
                                                                                      `YMM/|Mb.  ,__
                                                                                   _,,-~`--..-~-'_,/`--,,,____
                                                                               `\,_,/',_.-~_..-~/' ,/---~~~"""`\
\n                                                                         _,_,,,\p\p/'    \,,-~'_,/`````-,7.
                                                                         `@v@`\\,,,,__   \,,-~~"__/` ",,/MMMMb.
                                                                          `--''_..-~~\   \,-~~""  `\_,/ `^YMMMMMb..
                                                                           ,|``-~~--./_,,_  _,,-~~'/_      `YMMMMMMMb.
                                                                         ,/  `\,_,,/`\    `\,___,,,/M/'      `YMMMMMMMb
                                                                                     ;  _,,/__...|MMM/         YMMMMMMMb
                                                                                      .' /'      dMMM\         !MMMMMMMMb
                                                                                   ,-'.-'""~~~--/M|M' \        !MMMMMMMMM
                                                                                 ,/ .|...._____/MMM\   b       gMMMMMMMMM
                                                                              ,'/'\/          dMMP/'   M.     ,MMMMMMMMMP
                                                                              / `\;/~~~~----...MP'     ,MMb..,dMMMMMMMMM'
                                                                            / ,_  |          _/      dMMMMMMMMMMMMMMMMB
                                                                            \  |\,\,,,,___ _/    _,dMMMMMMMMMMMP".emmmb,
                                                                             `.\  gY.     /      7MMMMMMMMMMP"..emmMMMMM
                                                                                .dMMMb,-..|       `.~~"""```|dMMMMP'MMP'
                                                                               .MMMMP^"""/ .7 ,  _  \,---~""`^YMMP'MM;
                                                                             _dMMMP'   ,' / | |\ \\  }          PM^M^b
                                                                          _,' _,  \_.._`./  } ; \ \``'      __,'_` _  `._
                                                                      ,-~/'./'| 7`,,__,}`   ``   ``        // _/`| 7``-._`}
                                                                     |_,}__{  {,/'   ``                    `\{_  {,/'   ``
                                                                     ``  ```   ``                            ``   ``


                                                    ████████╗██╗░░██╗███████╗  ░██████╗████████╗░█████╗░██████╗░████████╗███████╗██████╗░
                                                    ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
                                                    ░░░██║░░░███████║█████╗░░  ╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░█████╗░░██████╔╝
                                                    ░░░██║░░░██╔══██║██╔══╝░░  ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
                                                    ░░░██║░░░██║░░██║███████╗  ██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗██║░░██║
                                                    ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝                                                                 
                                                                 
''')

    print(" ")
    print("")
    print(" ")
    print("                                                  ###########################################################################################")
    print("                                                                                             Play")
    print("                                                                                           Credits")
    print("                                                                                             Exit")
    print("                                                  ###########################################################################################")
    title_screen_select()

#death seq - not currently being used.     
def deathseq():
     #if (char['HP'] <= 0):
        print ("You have been slain by the" + enemy_pick)
        time.sleep(4)
        endscr()

#function to replay the game or exit after you die
def endscr():        
    clrscrn()
    redo = input ("Thank you for playing our game, If you would like to play again press 1, to exit press 2\n") 
    if redo == ("1"):
        title_screen()
    elif redo == ("2"):
        os.system(exit)

def prologue(char):
    #base stats prior to class selection come from char(stats)
    
    #get a PC name logged and recorded
    typing ("Welcome adventurer.\n")
    time.sleep(1)

    typing("Welcome to The Starter, are you ready for a text based RPG experience?\n")
    time.sleep(2)
    typing("Of course you are. Great lets start!\n")
    time.sleep(1)
    #player name
    typing ("Lets start with your name, what should I call you?\n")
    pcname = input()
    time.sleep(1)
    typing ("\n\nVery nice to meet you " + pcname +", now i think its time for you to meet your trusty companion.\nNo RPG is the same without a companion, even a text based one.\n")
    time.sleep(1)

    lines = open('Animals1.txt').read().splitlines()
    dewi = random.choice(lines)

    typing("Lets introduce you to Dewi.\nDewi will be your trusted companion.\nWhat is Dewi I hear you ask? well he is a " +dewi+"\n\n")

    #class selection
    typing("Now then " + pcname + ", now for the important bit, which class best suits you?\n1.Warrior\n2.Thief\n3.Soilder\n\n\n")
    question2 = input()

    #warrior stats
    if question2 == "Warrior" or question2 == "warrior" or question2 == "1":
        char['HP'] = char['HP'] * 5
        char['DEF'] = char['DEF'] * 3
        char['ATK'] = char['ATK'] * 3
        pcclass = "Warrior" 
        typing ("You are a warrior! \nYou are a brave fighter, Fearless in life, a man of very few words but knows exactly how to slay his enimies.\n")

    #thief stats
    elif question2 == "Thief" or question2 == "thief" or question2 == "2":
        char['HP'] = char['HP'] * 3
        char['DEF'] = char['DEF'] * 3
        char['ATK'] = char['ATK'] * 5
        pcclass = "Thief"
        typing ("You are a thief!\n.You are a master of stealth, you hide in the shadows. You relish it when your enemies underestimate you because of your size.\n")
        #soilder stats
    elif question2 == "Soldier" or question2 == "soldier" or question2 == "3":
        char['HP'] = char['HP'] * 3
        char['DEF'] = char['DEF'] * 5
        char['ATK'] = char['ATK'] * 3
        pcclass = "Soldier"
        typing ("You are a soldier.\nYou probably lead a very boring life if you chose soldier. You hit hard and can take hits blah blah blah.... lets get on with it.\n")


    clrscrn()
    time.sleep(2)    
    typing ("Well then my new " + pcclass + ", I hope you are happy with the results you have here as you cant change them.\n")
    time.sleep(2)
    print("Health:     " + str(char['HP']))
    print("Attack:    " + str(char['ATK']))
    print("Defence:    " + str(char['DEF']))

    time.sleep(5)
    clrscrn()

    

    typing("So are you ready for an adventure then? \nStep forward, through this door your first room awaits. " + pcname + ".\n")
    room1()




































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
