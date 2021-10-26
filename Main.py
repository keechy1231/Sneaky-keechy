#this is the main game

import os
import time #importing time
import sys


def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
		
time.sleep(7)		

typing ("Welcome to our first little game\n\n\n\n\nCreated by;")

time.sleep(1)

mystring = '''			:::    ::: :::::::::: :::::::::: ::::::::  :::    ::: :::   :::           :::     ::::    ::: :::::::::         ::::::::  ::::    ::: ::::::::::     :::     :::    ::: :::   ::: 
				:+:   :+:  :+:        :+:       :+:    :+: :+:    :+: :+:   :+:         :+: :+:   :+:+:   :+: :+:    :+:       :+:    :+: :+:+:   :+: :+:          :+: :+:   :+:   :+:  :+:   :+: 
				+:+  +:+   +:+        +:+       +:+        +:+    +:+  +:+ +:+         +:+   +:+  :+:+:+  +:+ +:+    +:+       +:+        :+:+:+  +:+ +:+         +:+   +:+  +:+  +:+    +:+ +:+  
				+#++:++    +#++:++#   +#++:++#  +#+        +#++:++#++   +#++:         +#++:++#++: +#+ +:+ +#+ +#+    +:+       +#++:++#++ +#+ +:+ +#+ +#++:++#   +#++:++#++: +#++:++      +#++:   
				+#+  +#+   +#+        +#+       +#+        +#+    +#+    +#+          +#+     +#+ +#+  +#+#+# +#+    +#+              +#+ +#+  +#+#+# +#+        +#+     +#+ +#+  +#+      +#+    
				#+#   #+#  #+#        #+#       #+#    #+# #+#    #+#    #+#          #+#     #+# #+#   #+#+# #+#    #+#       #+#    #+# #+#   #+#+# #+#        #+#     #+# #+#   #+#     #+#    
				###    ### ########## ########## ########  ###    ###    ###          ###     ### ###    #### #########         ########  ###    #### ########## ###     ### ###    ###    ###    '''			

print (mystring)	


time.sleep(5)
print("\033[H\033[J")

typing ("In this game you will encounter random events against random enemies, everytime you play this game it will play differently.\n\n\n\n\n")


input ("Press Enter to Begin")

print("\033[H\033[J")
from Prologue import Prologue #imorting Prologue into this #bring Prologue to the game
Prologue()




