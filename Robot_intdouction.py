class robot:
    def __init__(self, name_a, name_b):
        self.name_a = name_a
        self.name_b = name_b

    def fight(self):
        print(self.name_a, "and", self.name_b, "are fighting!")

ob = robot("Tom", "Jerry")
ob.fight()
        