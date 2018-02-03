import math

#print
print("hello world!")

#store input as variable "name"
name = input("What is your name?\n")

#Print Banner
print ("Hello " + name + ", let me print your banner...\n")
print ("-----------\n.::" + name + "::.\n-----------")

#casting (turn string to integer)
number = input("enter a number\n")
answer = int(number) * 3 #int converts to integer
print("Your number trippled is: " + str(answer) + "!\n") #can't display int!

#calculate area of a circle from radius.
#area = pi r ^2
print("pi is " + str(math.pi) + "\n")
print("I will now calculate the area of a circle from its radius.\n")
radius = input("Enter a radius: ")
#do some math (import math)
area = math.pi * (int(radius) * 2)
print("The area of a circle with radius " + radius + " is: " +  str(area) + ".\n")

#The Boolean challenge
print("is \"Some text\" the same as \"some text\"?\n")
text1 = "Some text"
text2 = "some text"
if text1 == text2:
    print("True\n")
else:
    print("False\n")
print("is -4 less than -6?\n")
if -4 < -6:
    print ("True\n")
else:
    print ("False\n")

 in "party!!!1" ?
print ("part" in "party!!!1")

#is my age valid?
age = input("Enter your age: \n")
print((int(age) > -1) and int(age) <125)


#Quiz!
print("Welcome to the Quiz!\n")
answer = input("are all apples red?\n")
if answer == "yes" or answer == "Yes" or answer == "true" or answer == "True" or answer == "y":
    print ("Well done :)")


#Lower case!
uppername = input("Enter caps to shrink:\n")
lowername = uppername.lower()
print(lowername)

