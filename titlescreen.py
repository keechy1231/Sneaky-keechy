#title screen test
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
        time.sleep(0.03)
        

        
def clrscrn():
    if os.name == 'posix':
        _=os.system("clear")
    else:
        _=os.system('cls')
        
def start():
    clrscrn()
    time.sleep(3)        
    typing ("Welcome to The Starter.  A text based RPG made by two people who have no coding experience.\n\n\n\n\nCreated by;\n")
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
    print ("\n\n\n\n\n\n\n\n\n\n\n\n")
   
    go = input("Please Press Enter to Begin\n")
    while 0 == 0 and go != 0:
        if go == ("") or go ==  (""):
                clrscrn()
                prologue()
        elif go != (""):
                typing ("Please Press Enter to Begin\n")
                go = 0
                go = input()

def title_screen_select():
    option = input()
    while 0 == 0 and option != 0:
        if option == ("play") or option ==  ("Play"):
                start()
        elif option == ("Credits") or option ==  ("credits"):
                credits()
        elif option == ("Exit")or option == ("exit"):
                sys.exit()
        elif option != ("Play") or option != ("play") or option != ("Credits") or option !=  ("credits") or option != ("Exit") or option != ("exit"):
                typing ("please input valid command\n")
                option = 0
        option = input
    
    
    
def title_screen():
    print ("")
    print("")
    print(" ")
    print("                                                  ###############################################################################################")
    print("                                                                                             Play")
    print("                                                                                           Credits")
    print("                                                                                             Exit")
    print("                                                  ###############################################################################################")
    title_screen_select()
    
def deathseq():
     #if (char['HP'] <= 0):
        print ("You have been slain")
        time.sleep(4)
        endscr()


def endscr():        #endscreen for when you die
    clrscrn()
    
    
    redo = input ("Thank you for playing our game, If you would like to play again Press 1, Press 2 to exit\n")
    if redo == ("1"):
        title_screen()
    elif redo == ("2"):
        credits()
    
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


title_screen()
