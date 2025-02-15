'''
4) Father has Skilled attribute of Gardenning and mother has Cooking , These skills are inherited
and child1 inherites skills of gardeing and child2 Cooking . Implement this
'''

class father:
    def __init__(self, skill):
        self.skill = skill

class mother:
    def __init__(self , skill):
        self.skill = skill
# Child1
class child1(father):
    def __init__(self, skill):
        super().__init__(skill)
    def show(self):
        print(f"Child 1's skilled at : {self.skill}")


# child2
class chil2(mother):
    def __init__(self, skill):
        super().__init__(skill)
    def show(self):
        print(f"Child 2's skilled at : {self.skill}")

# For Ronoker er boro bhai
Child1_object = child1("Gardening")
Child1_object.show()

# For amr Bondhu Ronok
Child2_object = child1("Cooking")
Child2_object.show()

