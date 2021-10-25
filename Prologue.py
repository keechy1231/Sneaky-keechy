import time
import os
#base stats prior to class selection
health = 10
stamina = 10
mana = 10
stealth = 10
strength = 10
#this will be our text based game 
#get a PC name logged and recorded
print ("welcome adventurer")
time.sleep(1)
print ("where should we begin?")
time.sleep(1)

#player title
print ("First off, how about your title, do you prefer mr, miss or something else?")
pcpronoun = input()
time.sleep(1)

#player name
print ("And now, how about a name. \nWhat should i call you")
pcname = input()

time.sleep(1)
print ("So you're "+pcpronoun+" "+ pcname+".\nIs that correct?")
time.sleep(1)
question1 = input()

#checking name is correct and fucking with the player a little
if question1 == "no" or question1 == "No":
    print("Oh is that so, then what is your name then?")
    pcname = input()
    print("So its "+ pcname+". Your sure this time?\nWell i dont really care what you say, i'm going to call you "+pcpronoun+" Indecisive for wasting my time")
    pcname = pcpronoun+" Indecisive"
elif question1 == "yes" or question1 == "Yes":
   print ("Okay, glad we got that right straight off the bat, you wouldnt believe how many people get their own name wrong.\nIts embarresing to be honest")
elif question1 != "yes" or question1 !="Yes" or question1 !="no" or question1 !="No" :
    print("What? thats not quite the answer to my question is it. I think im going to call you "+pcpronoun+" Ignoramus.")
    pcname = pcpronoun+" Ignoramus"
time.sleep(1)

#class selection
print("next question for you then " + pcname + ", what is your class?\n1.Warrior\n2.Thief\n3.Mage\n4.Priest\n5.Paladin")
question2 = input()

#warrior stats
if question2 == "Warrior" or question2 == "warrior" or question2 == "1":
    health = health * 5
    stamina = stamina * 3
    mana = mana * 1
    stealth = stealth * 2
    strength = strength * 4
    print("A warrior you will be!\nYour health and strength are you best assets but you can still hide as a last resort.\nI wouldn't put any faith in you magic skills though if I were you.")

#thief stats
elif question2 == "Thief" or question2 == "thief" or question2 == "2":
    health = health * 1
    stamina = stamina * 4
    mana = mana * 3
    stealth = stealth * 5
    strength = strength * 2
    print("A thief you will be!\nYour stealth and stamina are you best assets but you can still fight as a last resort.\nUnfortuanately for you though, you are very squishy.")

#mage stats
elif question2 == "Mage" or question2 == "mage" or question2 == "3":
    health = health * 2
    stamina = stamina * 4
    mana = mana * 5
    stealth = stealth * 3
    strength = strength * 1
    print("A Mage you will be!\nYour mana and stamina are you best assets but you have a little toughness just in case.\nBut you cant open that jar from the back of the cupboard.")

#priest stats
elif question2 == "Priest" or question2 == "priest" or question2 == "4":
    health = health * 5
    stamina = stamina * 2
    mana = mana * 4
    stealth = stealth * 1
    strength = strength * 3
    print("A Priest you will be!\nYour toughness and mana are you best assets but you have a little stamina if you need to run from a fight.\nJust dont try to hide, your like a holy flashlight.")

#paladin stats
elif question2 == "Paladin" or question2 == "paladin" or question2 == "5":
    health = health * 3
    stamina = stamina * 2
    mana = mana * 4
    stealth = stealth * 1
    strength = strength * 5
    print("A Paladin you will be!\nYour strength and mana are you best assets but you have okay cardio after all that jogging.\nYou are not really the best at hiding in that plate mail though *$%CLING?!@CLANG@#*.")

print("So are you ready for an adventure then? \nOf course you are why else would you be here "+pcname+".")
