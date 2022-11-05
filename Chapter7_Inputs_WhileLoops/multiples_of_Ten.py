"""
Ask the user for a number, and then report wether
the number is a multiple of 10 or not
"""

promtForNumber = input("Hi, please provide me a number to see if it is multiple of 10: ")

if int(promtForNumber)%10 == 0:
    print(f"The number {promtForNumber} is multiple of 10")
else:
    print("not  a multiple of 10")