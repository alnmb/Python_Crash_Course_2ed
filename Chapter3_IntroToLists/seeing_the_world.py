"""
“3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
1.- Store the locations in a list. Make sure the list is not in alphabetical order.
2.- Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
3.- Use sorted() to print your list in alphabetical order without modifying the actual list.
4.- Show that your list is still in its original order by printing it.
5.- Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
6.- Show that your list is still in its original order by printing it again.
7.- Use reverse() to change the order of your list. Print the list to show that its order has changed.
8.- Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
9.- Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
10.-Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.”

"""

places = ["Tokyo", "Rome", "New York", "Vatican", "Madrid"]

print("List in order")
print(places)

print("List in alphabetical order")
print(sorted(places))

print("Original List: ")
print(places)

print("List reversed")
print(sorted(places, reverse=True))

print("List original")
print(places)

print("List reversed altered")
print(places.reverse())

print("Looks like original")
print(places)

print("Sorted List")
print(places.sort())

print("Reversed sorted")
print(places.sort(reverse=True))
