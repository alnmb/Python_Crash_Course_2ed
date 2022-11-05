"""“
Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.”
"""

millionList = list(range(1,1000001))

print(f"Min value:{min(millionList)}")
print(f"Max value:{max(millionList)}")
print(f"The sum of a million is:{sum(millionList)}")