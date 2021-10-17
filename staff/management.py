from base.mammal import Mammal


class ManagementStaff(Mammal):

    def declare_role(self, role):
        print("I am " + role)


