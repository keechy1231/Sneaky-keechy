#testing picking a random comanion called dewi



#print(random.choice(open("Animals1.txt","r").readline().split()))   #


import random



lines = open('Animals1.txt').read().splitlines()

Dewi = random.choice(lines)
print(companion)