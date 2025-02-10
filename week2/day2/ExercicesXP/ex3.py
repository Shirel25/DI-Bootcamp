from ex2 import *
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True 

    def play(self, *args):
        if len(args) == 1:
            dog_names = args[0]
        else:
            dog_names = ", ".join(args[:-1]) + f", and {args[-1]}"
        return f"{dog_names} all play together."

    def do_a_trick(self):
        training = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained:
            rand = random.choice(training)
            print(self.name + " " + rand)
        else:
            print(self.name + " is not trained yet and cannot do any tricks.")


pet1 = PetDog("Chocolat", 5, 22)
pet1.train()  

pet2 = PetDog("Cookie", 1, 8)

print(pet1.play("Rocky", "Oreo", "Joy", "Chocolat"))
pet1.do_a_trick()
pet2.do_a_trick()