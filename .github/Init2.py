class Enemy:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
george = Enemy(14)

jason.get_energy()
george.get_energy()

# You call enemies with the init