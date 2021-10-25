import time


#this will be our text based game 
#get a PC name logged and recorded
print ("welcome adventurer")
time.sleep(2)
print ("where should we begin?")
time.sleep(2)
print ("First off, how about a pronoun, do you prefer mr, miss or something else?")
pcpronoun = input()
time.sleep(2)
print ("And now, how about a name. \nWhat should i call you")

pcname = input()

time.sleep(3)
print ("So you'r "+pcpronoun+" "+ pcname+".\nIs that correct?")

question1 = input()

if question1 == "no" or question1 =="No":
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
print("So are you ready for an adventure then? \nOf course you are why else would you be here")
