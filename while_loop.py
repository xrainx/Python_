import random

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0; #iterator
while(i <= 20):
    if(i%2 == 0): #if even
        print(i)
    elif(i == 9):
        break # jump out the loop.
    else:
        i += 1 # i = i+1
        continue # skip everything and restart.
    i += 1
