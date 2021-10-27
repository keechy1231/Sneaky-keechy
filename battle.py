import sys
import time
import os
import random

def enterbattlescenario():
    


enemylist = {
    "Imp"    : {'ehp':10, 'eatk':4, 'edef':2, 'expgain':13},
    "Ogre"   : {'ehp':15, 'eatk':1, 'edef':12, 'expgain':13},
    "Dwarf"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Small Handed Sweedish Fellow" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Giant"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Goblin" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Ghoul"  : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
    "Psycho" : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13}}



enemypick = (random.choice(list(enemylist.items())))


epickname = enemypick[0]
epick = dict(enemypick[1])


print(epickname)
print(epick)
print(epick['ehp'])