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
        time.sleep(0.05)
        
def ftyping(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
        
def styping(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
        
def clrscrn():
    if os.name == 'posix':
        _=os.system("clear")
    else:
        _=os.system('cls')
        
def start():
    clrscrn()
    time.sleep(3)        
    ftyping ("Welcome to our first little game\n\n\n\n\nCreated by;\n")
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
    clrscrn()
    styping ("In this game you will encounter random events against random enemies, everytime you play this game it will play differently.\n\n\n\n\n")
    input ("Press Enter to Begin")
    clrscrn()
    from Prologue import Prologue #imorting Prologue into this #bring Prologue to the game
    
    Prologue()

def title_screen_select():
    option = input()
    while 0 == 0 and option != 0:
        if option == ("play"):
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
    
    
def credits():
    clrscrn()
    print ("keechy and sneaky are sad sad people and sat here and coded a game when they had no knowledge of python")
    input ("Press Enter to return to Title Screen")
    clrscrn()
    title_screen()

title_screen()
