"""
“Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.

Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
print a message to that person letting them know you’re sorry you can’t invite them to dinner.

Print a message to each of the two people still on your list, letting them know they’re still invited.

Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.”

"""

invitees_to_dinner = ["Tesla", "Michael Jackson", "Maria de Jesus"]

message = " hi would you like to come to my dinner tonight? "

print(invitees_to_dinner[0]+""+message)
print(invitees_to_dinner[1]+""+message)
print(invitees_to_dinner[2]+""+message)
print()
invitees_to_dinner.insert(0,"Dave Mustaine")
invitees_to_dinner.insert(2, "Paul Stanley")
invitees_to_dinner.append("Bruce Dickinson")
print()
print(invitees_to_dinner[0]+""+message)
print(invitees_to_dinner[1]+""+message)
print(invitees_to_dinner[2]+""+message)
print(invitees_to_dinner[3]+""+message)
print(invitees_to_dinner[4]+""+message)
print(invitees_to_dinner[5]+""+message)

print()
print("Ups I have space only for two")
print("Sorry, "+invitees_to_dinner[-1])
invitees_to_dinner.pop()
print("Sorry, "+invitees_to_dinner[-1])
invitees_to_dinner.pop()
print("Sorry, "+invitees_to_dinner[-1])
invitees_to_dinner.pop()
print("Sorry, "+invitees_to_dinner[-1])
invitees_to_dinner.pop()

print(invitees_to_dinner[0]+" you are welcome to come")
print(invitees_to_dinner[1]+" you are welcome to come")

del invitees_to_dinner[1]
del invitees_to_dinner[0]

print("Empty list ")
print(invitees_to_dinner)