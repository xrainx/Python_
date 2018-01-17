print("Welcome! type any number.")
print("type \"quit\" to exit")
if exit != 0:
    loop=0
loop = 1
while loop == 1:

    x = input("--> ")

    if x != "quit" :
        x = int(x) #converts to integer


    if x > 0:
        print("input is greater than 0!")
        if x < 100:
            print("input is also less than 100!")
            if x == 10:
                print("input is 10!")


    if x < 0:
        print("input is less than 0!")

    if x == 0:
        print("input is zero!")

    if x == quit:
        exit = 1
