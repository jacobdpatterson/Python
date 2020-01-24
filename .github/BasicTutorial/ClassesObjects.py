class Enemy: # You capitalize classes
    life = 3

    def attack(self):
        print('Oof!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I've been slain!")
        else:
            print(str(self.life) + " life left.")

# An object is a way to access the stuff in your class.

enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()

enemy2 = Enemy()
enemy2.attack()
enemy2.attack()
enemy2.checkLife()