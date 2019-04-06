'''
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
    if number % 4 == 0:
        print("The number is a multiple of 4")
else:
    print("The number is odd")

num = int(input("Enter a number: "))
check = int(input("Enter another number: "))

if check % num == 0:
    print(str(num) ,"is divisible by" ,str(check))
else:
    print(str(num) ,"is not divisible by", str(check))
