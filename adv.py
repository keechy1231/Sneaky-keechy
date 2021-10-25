import time

#this will be our text based game 
#get a PC name logged and recorded
print ("welcome adventurer")
time.sleep(2)
print ("where should we begin?")
time.sleep(2)
print ("how about a name. \nWhat should i call you")

pcname = input()

time.sleep(3)
print ("So you'r "+ pcname+".\nIs that correct?")

if input("no")or input("No"):
    print