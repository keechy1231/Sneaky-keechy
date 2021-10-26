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
	
typing ("Current level:" +str(lvl)+"\n")
print ("Current xp:" + str(round(xp / lvlnext,2)*100)+"%")
typing ("To next level:"+ str(lvlnext)+"\n")

