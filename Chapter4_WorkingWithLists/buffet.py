"""
“Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

1. Use a for loop to print each food the restaurant offers.
2. Try to modify one of the items, and make sure that Python rejects the change.
3. The restaurant changes its menu, replacing two of the items with different foods. 
   Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.”

"""

basic_foods = ("sandwich", "nuggets", "pizza", "spagetti", "sushi")

for bfood in basic_foods:
    print(bfood)

print("\n")
basic_foods = ("tuna","salad", "keto burger")

for bfood in basic_foods:
    print(bfood)