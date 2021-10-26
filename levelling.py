import sys
import time
import os


def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

lvl = 1
xp = 14
lvlnext = 10

while xp >= lvlnext:
	lvl += 1
	xp = xp - lvlnext
	lvlnext = round(lvlnext * 1.2)
	
typing ("Current Level:             " + str(lvl)+"\n")
#typing ("Current Level EXP:         " + str(round(xp / lvlnext,2)*100)+"%\n") #my original code - one below looks cleaner
typing ("Current level EXP:         {}%\n" .format(int((xp / lvlnext)*100)))
typing ("EXP needed for next Level: " + str(lvlnext)+"\n")

