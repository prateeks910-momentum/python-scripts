class Dog():
    species='mammal'
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        print(f'{self.name} of breed {self.breed} says woof!')


my_dog = Dog(breed="doberman", name='Jimmy')
print(Dog.species)
print(my_dog.breed)
my_dog.bark()