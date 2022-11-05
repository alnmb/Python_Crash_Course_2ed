"""write a program that polls users about their
dream vacation. write a prompt similar to
'if you could visit one place in the world, where
would you go?' 
include a block of code that prints the results of the poll"""

from asyncore import poll


dreams = {}
poll_active = True

while poll_active:
    promptForName = input('Please provide your name: ')
    promtForDream = input("\nif you could visit one place in the world, where would you go?: \n")

    dreams[promptForName] = promtForDream

    repeatProgram = input("Would you like to let another person respond? (yes/no) ")
    if repeatProgram == 'no':
        poll_active = False

print('\nPrinting results')
for name, dreams in dreams.items():
    print(f"{name} would like to go to {dreams}")