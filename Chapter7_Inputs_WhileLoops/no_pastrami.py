"""Using the list sandwich_orders, make sure the
sandwich 'pastrami' appears in the list at least 
three times. add code near the begining of your
program to print a message saying the deli has run
out of pastrami. then use a while loop to remove
all occurrencies of 'pastrami' from the list.
make sure no pastrami sandwiches end up in finished"""


sandwich_orders = ['chicken','egg','pastrami', 'tuna','grilled cheese','pastrami','nutella', 'ham', 'pastrami']
finished_sandwiches = []

#removing pastrami sandwiches
print("Sorry, we are out of pastrami\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I have prepared your {current_order} sandwich\n")
    finished_sandwiches.append(current_order)
    

print("List of sandwiches made:\n")
for prepared in finished_sandwiches:
    print(prepared)

print('\n')