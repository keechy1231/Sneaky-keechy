#this file is to test a room system
import os
import sys
import cmd


def clrscrn():
    if os.name == 'posix':
        _=os.system("clear")
    else:
        _=os.system('cls')


def room1():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("to your East there is a big black door, its open.  To your West there is a dark corridor, which way will you go? (Type E or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "E" or mvnt == "e":
            room3()
        elif mvnt == "W" or mvnt == "w":
            room2()
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("W") or mvnt !=  ("w"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    clrscrn()
 
 
def room2():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(Type S or E to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "S" or mvnt == "s":
            room4()
        elif mvnt == "E" or mvnt == "e":
            room1()
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("S") or mvnt !=  ("s"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    


def room3():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(Type S or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "S" or mvnt == "s":
            room5()
        elif mvnt == "W" or mvnt == "w":
            room1()
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("S") or mvnt !=  ("s"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    

def room4():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(Type N or E to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            room2()
        elif mvnt == "E" or mvnt == "e":
            room6()
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("N") or mvnt !=  ("n"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()

def room5():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(Type N or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            room3()
        elif mvnt == "W" or mvnt == "w":
            room6()
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("N") or mvnt !=  ("n"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    clrscrn()


def room6():
    clrscrn()
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("(THE BOSS ROOM IS TO THE NORTH Type W or E OR N to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "N" or mvnt == "n":
            bossroom()
        elif mvnt == "W" or mvnt == "w":
            room4()
        elif mvnt == "E" or mvnt == "e":
            room5()
        elif mvnt != ("W") or mvnt != ("w") or mvnt != ("N") or mvnt != ("n") or mvnt != ("E") or mvnt !=  ("e"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
    

def bossroom():
    clrscrn()
    print ("THIS IS THE BOSS BITCH") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
room1()
