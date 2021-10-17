from staff.management import ManagementStaff
from animals.elephant import Elephant
from guests.kids import KidGuest
from guests.adults import AdultGuest

accountant = ManagementStaff("Alice", 44, "Human")
accountant.introduce()
accountant.declare_spiece()

boss = ManagementStaff("Bob", 50, "Human")
boss.declare_role("Boss")

elephant = Elephant("Stephen", 12, "Elephant")
elephant.introduce()
elephant.declare_spiece()
elephant.eat_elephant_specific_food("Roots")

first_adult_guest = AdultGuest("Rick", 33, "Human")
first_adult_guest.introduce()
first_adult_guest.declare_role()

first_kid_guest = KidGuest("Alan", 11, "Human")
first_kid_guest.introduce()
first_kid_guest.amount_of_money_to_spend()



