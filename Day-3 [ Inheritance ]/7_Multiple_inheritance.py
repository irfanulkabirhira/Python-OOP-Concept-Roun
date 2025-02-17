# Multiple Inheritance --> example is me (Multiple Parent , Single Child)
'''
class Father:
    pass
class Mother:
    pass
# Intermediate Class  - inheriting from father and Mother
class child(Father, Mother):
    pass

'''
'''
A father and Mother Class , inherited to their Child Hira(Both contain name,age attribute)
and Hira contain with his name only
So , Now show father, mother and hira's detail

'''

class father:
    def __init__(self, father_name , father_age):
        self.father_name = father_name
        self.father_age = father_age
    def show_father(self):
        print(f"Father's name : {self.father_name} , Father's Age : {self.father_age}")
class mother:
    def __init__(self, mother_name , mother_age):
        self.mother_name = mother_name
        self.mother_age  = mother_age
    def show_mother(self):
        print(f"Mother's name : {self.mother_name} , Mother's Age : {self.mother_age}")

class Hira(father, mother):
    def __init__(self, father_name, father_age, name):
        super().__init__(father_name, father_age)
        self.name = name
    def show_hira(self):
        print(f"Name : {self.name}")

# creating object for Everyone
print("Father's Detail")
father1 = father('Abu Taher ', 58)
father1.show_father()

print("\nMother's Detail")
mother1 = mother('laila Begum', 56)
mother1.show_mother()

print("\nHira's Detail")
hira1 = Hira('Abu Taher', 43, 'hira')
hira1.show_hira()