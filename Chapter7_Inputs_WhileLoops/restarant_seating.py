"""Write a program that asks the user how many
people are in their dinner group.
If the ansert is more than eight, print a message
saying they´ll have to wait for a table.
otherwise, report that their table is ready"""

promptForPeople = input("Hi welcome,\nHow many people are in this group?: ")

if int(promptForPeople) >= 8:
    print("Sorry we don't have room for a big group please wait a moment for a table")
else:
    print("Welcome!, your table  is ready")