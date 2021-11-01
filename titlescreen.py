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
                endscr()
        elif option != ("Play") or option != ("play") or option != ("Credits") or option !=  ("credits") or option != ("Exit") or option != ("exit"):
                typing ("please input valid command\n")
                option = 0
        option = input()
    
    
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
    
def deathseq():
     #if (char['HP'] <= 0):
        print ("You have been slain by the" + enemy_pick)
        time.sleep(4)
        endscr()


def endscr():        #endscreen for when you die
    clrscrn()
    
    
    redo = input ("Thank you for playing our game, If you would like to play again Press 1, Press 2 to exit\n")
    if redo == ("1"):
        title_screen()
    elif redo == ("2"):
        credits()
    

title_screen()
