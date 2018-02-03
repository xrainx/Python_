#Dr. Love
print("Hello, are you made for each other?\n")
name1 = input("Your name: ")
name2 = input("Your crush: ")

# set initial value
love = 100

weight1 = 100 / len(name1)
for char in name1:
    if char.lower() not in ['l','o','v','e','s']:
        love -= weight1

weight2 = 100 / len(name2)
for char in name2:
    if char.lower() not in ['l','o','v','e','s']:
        love -= weight2

result = (int(weight1) + int(weight2) / 2) 
print("You are " + str(result) + "% made for each other!") 
