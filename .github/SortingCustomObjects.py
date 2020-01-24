from operator import attrgetter

class User:

    def __init__(self, x, y): # - Do this initially always.
        self.name = x
        self.user_id = y

    def __repr__(self): # - String representation of this object.
        return self.name + " : " + str(self.user_id)


users = [
User('Abe1', 131),
User('Abe2', 13),
User('Abe3', 1553),
User('Abe4', 1135),
User('Abe5', 113),
User('Abe6', 135),
User('Abe7', 133),
User('Abe8', 123)
]

# - Sorts name by default.

for user in users:
    print(user)

# We want to sort by name.

print('==================')
for user in sorted(users,key=attrgetter('name')):
    print(user)

# We want to sort by ID.

print('==================')
for user in sorted(users,key=attrgetter('user_id')):
    print(user)