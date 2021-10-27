import sys
import time
import os
import random


enemylist = {'imp' : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13},
             'orc' : {'ehp':10, 'eatk':11, 'edef':12, 'expgain':13}}



print(random.choice(list(enemylist.values)))
