from base.mammal import Mammal


class Elephant(Mammal):

    def eat_elephant_specific_food(self, food_type):
        print("eating " + food_type)

    def declare_spiece(self):
        print("My spiece is elephant")


elephant_joe = Elephant("Joe", 23, "Elephant")
elephant_joe.introduce()
elephant_joe.declare_spiece()
elephant_joe.eat_elephant_specific_food("roots")


