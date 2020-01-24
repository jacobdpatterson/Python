from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Poopy', 'lname': 'McPoop'},
    {'fname': 'Tom', 'lname': 'O\'Rourke'},
    {'fname': 'Farty', 'lname': 'McPoopfarts'},
    {'fname': 'Chadwicke', 'lname': 'O\'Rourke'},
    {'fname': 'PooFartMcPoop', 'lname': 'O\'Rourke'},
    {'fname': 'PooFartMcPoop', 'lname': 'O\'Finnegan'},
    {'fname': 'PooFartMcPoop', 'lname': 'O\'Sullivan'},
    {'fname': 'PooFartMcPoop', 'lname': 'O\'Learehy'}
]

# - Bad way to sort. PooFartMcPoop gives you issues.
print('------')
for x in sorted(users, key=itemgetter('fname')):
    print(x)

# - Bad way to sort. O'Rourke gives you issues.
print('------')
for x in sorted(users, key=itemgetter('lname')):
    print(x)

# - This prints by first name and further by last name. Should be perfect.

print('------')
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)