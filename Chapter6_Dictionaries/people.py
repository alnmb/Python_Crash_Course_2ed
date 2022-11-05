"""
“6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person.”

"""


person = {
    'firstname':'Alan',
    'lastname':'Martinez',
    'age':'29',
    'city':'Monterrey'
}

person2 = {
    'firstname':'Erik',
    'lastname':'Martinez',
    'age':'41',
    'city':'Monterrey'
}

person3 = {
    'firstname':'Brenda',
    'lastname':'Martinez',
    'age':'45',
    'city':'Monterrey'
}

people =[person,person2,person3]

for person in people:{
    print(person['firstname']+" "+person['lastname']+" is from "+person['city'])
}