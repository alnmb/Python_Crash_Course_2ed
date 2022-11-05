"""“
You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.”
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
