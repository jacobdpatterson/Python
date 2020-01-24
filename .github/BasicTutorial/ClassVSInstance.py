class Girl: #class itself
    gender = 'female'

    def __init__(self,name):
        self.name = name

r = Girl('Rachel') # Instance of class
s = Girl('Stanky') # Instance of class
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)


