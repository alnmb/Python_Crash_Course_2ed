"""
A movie teather charges differnt tickets prices
depending on a persons age. If a person is under
the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and
if they are over age 12, the ticket is $15.

write a loop in which you ask the users their age
and then tell them the cost of their ticket
"""

promptForAge = "Hi, welcome to the movie teather"
promptForAge +=  "\nplease provide your age: "
    
while True:
    age = input(promptForAge)

    if age == "quit":
        break
    else:
        age = int(age)

    if age < 3:
        print(f"\nYour age is {age}. so your ticket is free\n")
    elif age >= 3 and age <12:
        print(f"\nYour age is {age}. so your ticket is $10\n")
    elif age >= 12:
        print(f"\nYour age is {age}. so your ticket is $15\n")
