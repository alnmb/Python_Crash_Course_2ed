"""
“ No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.

If the list is empty, print the message We need to find some users!
Remove all of the usernames from your list, and make sure the correct message is printed.”

"""

usernames = ["alan","magda", "lesly", "poncho", "alex", "admin"]

if usernames:
    for user in usernames:
        if user != "admin":
            print(f"Good Morning {user}")
        else:
            print(f"Hi mister {user} would you like to see a status report?")
else:
    print("we need to set up some users")