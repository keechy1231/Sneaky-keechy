import sys
import time
import os
import random

#enemy dictionary for the function to be defined
enemylist = {
    "Imp"    : {'ehp':10, 'eatk':4, 'edef':2, 'expgain':13},
    "Ogre"   : {'ehp':15, 'eatk':1, 'edef':12, 'expgain':13},
    "Dwarf"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Tiny Hands" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Giant"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Goblin" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Ghoul"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Psycho" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13}}


#picks a random enemy from the dictionary enemylist
enemypick = (random.choice(list(enemylist.items())))

epickname = enemypick[0]
epick = dict(enemypick[1])

#epickname shows the chosen enemys name
#epick is the chosen enemys stats as a dictionary

#https://patorjk.com/software/taag/#p=display&f=Big%20Chief&t=Tiny%20Hands
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

input()