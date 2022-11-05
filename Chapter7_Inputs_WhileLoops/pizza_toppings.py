"""
Write a loop that promtps the user 
to enter a series of pizza toppings until 
they enter
a 'quit' value. As the enter each topping,
print a message saying 
you will add that topping to their pizza


"""

toppings=""
while toppings != 'quit':
    toppings = input("Hi, please provide a pizza topping: ")
    if toppings != 'quit':
        print(toppings)
        continue
    else:
        break