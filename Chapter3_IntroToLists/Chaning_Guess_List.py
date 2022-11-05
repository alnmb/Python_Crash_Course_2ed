"""
“You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still in your list.”

"""

from email import message


invitees_to_dinner = ["Tesla", "Michael Jackson", "Maria de Jesus"]

message = " hi would you like to come to my dinner tonight? "

print(invitees_to_dinner[0]+""+message)
print(invitees_to_dinner[1]+""+message)
print(invitees_to_dinner[2]+""+message)

print()
print("Seems like "+invitees_to_dinner[0]+" won't be able to join us")
print()
invitees_to_dinner.remove("Tesla")
invitees_to_dinner.append("Fidel Galvan")

print(invitees_to_dinner[0]+""+message)
print(invitees_to_dinner[1]+""+message)
print(invitees_to_dinner[2]+""+message)
