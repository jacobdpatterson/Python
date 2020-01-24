class Parent():

    def print_last_name(self):
        print('Roberts')

class Child(Parent): # Looks for parent, gets everything in class, pass it on to this class.

    def print_first_name(self):
        print('Bucky')

    '''  def print_last_name(self): #This overrides the parent function.
        print('Snitzleberg') '''

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()