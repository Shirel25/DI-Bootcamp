class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name 
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("Rex", 50)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

print("\n================================")
sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

print("\n================================")

if davids_dog.height > sarahs_dog.height:
    bigger_dog = davids_dog
else:
    bigger_dog = sarahs_dog
print(bigger_dog.name)

# dogs = [davids_dog, sarahs_dog]
# bigger = dogs[0]
# if dogs[1].height > bigger.height:
#     bigger = dogs[1]
# print(bigger.name)