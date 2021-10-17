class Mammal:
    species = 'mammal'

    def __init__(self, name, age, spiece):
        print("base class created")
        self.name = name
        self.age = age
        self.spiece = spiece

    def introduce(self):
        print("My name is " + self.name + " and I am " + str(self.age) + " years old")

    def declare_spiece(self):
        print("My spiece is " + self.spiece)
