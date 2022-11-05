"""Make a list called sandich_orders and fill it
with the names of various sandwiches.
then make an empty list called finished_sahdwiches.
Loop thru the list of sandwich orders and print
a message for each order, such as 'I made your tuna sandwich'
as each sandwich is made, move it to the list of
finished sandwiches. after all the sandwiches have
been made, print a message listing each sandwich
that was made"""

sandwich_orders = ['chicken','egg', 'tuna','grilled cheese','nutella', 'ham']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I have prepared your {current_order} sandwich\n")
    finished_sandwiches.append(current_order)
    

print("List of sandwiches made:\n")
for prepared in finished_sandwiches:
    print(prepared)

print('\n')