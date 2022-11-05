"""
“ Rivers: Make a dictionary containing three major rivers and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile 
“Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.”

"""

rivers = {
    'brazil':'amazonas',
    'egypt':'nilo',
    'china':'yangtse'
    }

#print river names
for river in rivers.values():
    print(f'The {river}')
#print name and description
print('\n')
for contry, river in rivers.items():
    print(f"The {river} runs on {contry}")

print('\n')
#print only names
for river in rivers.values():
    print(river)

#print only locations
print('\n')
for location in rivers.keys():
    print(location)