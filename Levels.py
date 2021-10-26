import sys
import time
import os




def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

#player starts at level 0
lvl = 1
xp = 5
lvlnext = 10

#base stats prior to class selection
health = 10
stamina = 10
stealth = 10
strength = 10
pcclass = "villager"


    while xp >= lvlnext:
	lvl += 1
	xp = xp - lvlnext
	lvlnext = round(lvlnext * 1.2)
	health = health + 5
	stamina = stamina + 5
	stealth = stealth + 5
	strength = strength + 5
	

typing ("Current Level:             " + str(lvl)+"\n")
#typing ("Current Level EXP:         " + str(round(xp / lvlnext,2)*100)+"%\n") #my original code - one below looks cleaner
typing ("Current level EXP:         {}%\n" .format(int((xp / lvlnext)*100)))
typing ("EXP needed for next Level: " + str(lvlnext)+"\n")
typing ("Health                     " + str(health )+"\n")
typing ("Stamina                    " + str(stamina )+"\n")
typing ("Stealth                    " + str(stealth )+"\n")
typing ("Strength                   " + str(strength )+"\n")