"""
“Favorite Fruit: Make a list of your favorite fruits, 
and then write a series of independent if statements that check for certain fruits in your list.

Make a list of your three favorite fruits and call it favorite_fruits.
Write five if statements. Each should check whether a certain kind of fruit is in your list. 
If the fruit is in your list, the if block should print a statement, such as You really like bananas!”

"""

fruits = ["banana", "mango", "orange"]

if "banana" in fruits:
    print(f"Te encantan las {fruits[0]}")
if "lemon" in fruits:
    print("no tenemos limones")
if "pepino" in fruits:
    print("no tenemos pepino")
if "mango" in fruits:
    print(f"te encantan los {fruits[1]}")
if "strawberry" in fruits:
    print("no tenemos fresas")