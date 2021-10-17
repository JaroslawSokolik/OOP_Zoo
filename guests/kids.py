from base.mammal import Mammal
import random


class KidGuest(Mammal):

    def declare_role(self):
        print("I am a Kid")

    def amount_of_money_to_spend(self):
        print("I have " + str(random.randint(0, 100)) + " złoty money to spend")

    def current_activity(self):
        activity = ["crying", "smiling", "upset", "sleeping"]
        print("I am " + (random.choice(activity)))


