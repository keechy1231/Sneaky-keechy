import sys
import time
import os


def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

lvl = 1
xp = 24
lvlnext = 10

while xp >= lvlnext:
	lvl += 1
	xp = xp - lvlnext
	lvlnext = round(lvlnext * 1.2)
	
print ("Current level:", lvl)
typing ("Current xp:", xp)
typing ("To next level:", lvlnext)

