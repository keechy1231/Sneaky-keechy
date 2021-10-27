import sys
import time
import os




def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

char = {'lvl': 1,
        'xp' : 0,
        'lvlnext' : 10}

stats = {'ATK': 10,
         'DEF': 5,
         'HP' : 10}

def level(char, stats):
    nATK, nDEF, nHP = 0, 0, 0
    while char['xp'] >= char['lvlnext']:
        char['lvl'] += 1
        char['xp'] = char['xp'] - char['lvlnext']
        char['lvlnext'] = round(char['lvlnext'] * 1.2)
        stats['ATK'] += 1
        stats['DEF'] += 1
        stats['HP'] +=1
        if char["xp"] < char["lvlnext"]:
            print("Congratulations you have reached level " + str(char["lvl"]))
            print("Current XP             " + str(char["xp"]))
            print("XP to next level       " + str(char["lvlnext"]))
            print("HP                   ^ " + str(stats["HP"]))
            print("Attack               ^ " + str(stats["ATK"]))
            print("Defense              ^ " + str(stats["DEF"]))

