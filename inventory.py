

char = {'lvl': 1,
        'xp' : 0,
        'lvlnext' : 10,
        'ATK': 10,
         'DEF': 5,
         'HP' : 10}


inventory = {'ATKpotion': 10,
        'HPpotion': 10}

HPpotion = inv['HPpotion']

ATKpotion = inv['ATKpotion']

def useHPpotion(HPpotion):

    print ("you are using HP potion")
    nhp = inventory['HPpotion'] + char['HP']
    print (nhp)


useHPpotion(HPpotion)

useATKpotion(ATKpotion)
    