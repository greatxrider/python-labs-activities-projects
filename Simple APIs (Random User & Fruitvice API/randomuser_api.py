from randomuser import RandomUser
import pandas as pd

# Create a random user
r = RandomUser()

#list of random 10 users

some_list = r.generate_users(10)
print(some_list)

#getting full name

name = r.get_full_name()
print(name)

#forloop print 10 users

for user in some_list:
    print(user.get_full_name(), " ", user.get_email())
    