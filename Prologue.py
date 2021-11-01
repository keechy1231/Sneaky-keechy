#file import
import time
import os
import sys
import random


#defineds presets
def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	
def clrscrn():
	if os.name == 'posix':
		_=os.system("clear")
	else:
		_=os.system('cls')

char = {'LVL': 1,
        'XP' : 0,
        'LVLNEXT' : 10,
        'ATK': 10,
         'DEF': 10,
         'HP' : 10}



def prologue(char):
    
    #base stats prior to class selection come from char(stats)
    
    #get a PC name logged and recorded
    typing ("Welcome adventurer.\n")
    time.sleep(1)

    typing("Welcome to The Starter, are you ready for a text based RPG experience?\n")
    time.sleep(2)
    typing("Of course you are. Great lets start!\n")
    time.sleep(1)
    #player name
    typing ("Lets start with your name, what should I call you?\n")
    pcname = input()
    time.sleep(1)
    typing ("\n\nVery nice to meet you " + pcname +", now i think its time for you to meet your trusty companion.\nNo RPG is the same without a companion, even a text based one.\n")
    time.sleep(1)

    with open('Animals1.txt', "r") as file:
        lines = file.readlines()
        dewi = lines[random.randint(0, len(lines)-1)]

    typing("Lets introduce you to Dewi.\nDewi will be your trusted companion.\nWhat is Dewi I hear you ask? Well he is a " +dewi+"\n\n")

    #class selection
    typing("Now then " + pcname + ", now for the important bit, which class best suits you?\n1.Warrior\n2.Thief\n3.Soilder\n\n\n")
    question2 = input()

    #warrior stats
    if question2 == "Warrior" or question2 == "warrior" or question2 == "1":
        char['HP'] = char['HP'] * 5
        char['DEF'] = char['DEF'] * 3
        char['ATK'] = char['ATK'] * 3
        pcclass = "Warrior" 
        typing ("You are a warrior! \nYou are a brave fighter, Fearless in life, a man of very few words but knows exactly how to slay his enimies.\n")

    #thief stats
    elif question2 == "Thief" or question2 == "thief" or question2 == "2":
        char['HP'] = char['HP'] * 3
        char['DEF'] = char['DEF'] * 3
        char['ATK'] = char['ATK'] * 5
        pcclass = "Thief"
        typing ("You are a thief!\n.You are a master of stealth, you hide in the shadows. You relish it when your enemies underestimate you because of your size.\n")
        #soilder stats
    elif question2 == "Soldier" or question2 == "soldier" or question2 == "3":
        char['HP'] = char['HP'] * 3
        char['DEF'] = char['DEF'] * 5
        char['ATK'] = char['ATK'] * 3
        pcclass = "Soldier"
        typing ("You are a soldier.\nYou probably lead a very boring life if you chose soldier. You hit hard and can take hits blah blah blah.... lets get on with it.\n")


    clrscrn()
    time.sleep(2)    
    typing ("Well then my new " + pcclass + ", I hope you are happy with the results you have here as you cant change them.\n")
    time.sleep(2)
    print("Health:     " + str(char['HP']))
    print("Attack:    " + str(char['ATK']))
    print("Defence:    " + str(char['DEF']))

    time.sleep(5)
    clrscrn()
    

    typing("So are you ready for an adventure then? \nStep forward, through this door your first room awaits. " + pcname + ".\n")
    room1()


prologue(char)