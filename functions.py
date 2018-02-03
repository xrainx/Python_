import random
import sys
import os

#fucntions: for reuse, and write more readable code.

def addNumber(fNum, lNum): # () parameters to receive
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1, 4)) #calls the function


#import from user
print("What is your name?")
name = sys.stdin.readline()
print ("Hello", name)
