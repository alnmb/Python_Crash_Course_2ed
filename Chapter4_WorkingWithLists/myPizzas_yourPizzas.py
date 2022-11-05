"""
“My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). 
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

1. Add a new pizza to the original list.
2. Add a different pizza to the list friend_pizzas.
3. Prove that you have two separate lists. 
   Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
   Make sure each new pizza is stored in the appropriate list.”

"""

pizzas = ["pepperoni", "quatre formaggi", "hawaian"]
friend_pizzas = pizzas[:]

pizzas.append("bacon")
friend_pizzas.append("ham")

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")

for fpizza in friend_pizzas:
    print(f"My friend favorite pizzas are: {fpizza}")