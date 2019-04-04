'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

name = input("Enter your name: ")
age = input("Enter your age: ")
yearsToOneHundred = 100 - int(age)
message = "Hello {}, you will be 100 years old in {} years.\n".format(name, yearsToOneHundred)
print(message)

'''
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
Print out that many copies of the previous message on separate lines.
'''

anotherNumber = input("Enter another number: ")
print(message * int(anotherNumber))
