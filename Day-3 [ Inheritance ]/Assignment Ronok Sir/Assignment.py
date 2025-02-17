'''
Write a program where some clases are (grandfather , father , mother , child1 , child2)
task :
1) Show all types of Inheritance that can be possible in this scenario
2) Give everyone a name and Job attribute , But it can be declared at most 2 time .
Figure out where they should be (jobs : farmer , banker , artist , Teacher , Programmer )
3) Implemented that grandfather has rented house , father owned one , and show child2 where lived
4) Father has Skilled attribute of Gardenning and mother has Cooking , These skills are inherited
and child1 inherites skills of gardeing and child2 Cooking . Implement this
5) lastly , show child1's and child2's  details

'''
# 1) Given Question contains all inheritance(single,Hierarchy,Multiple,Multi-level,Hybrid Inheritssnce)
# 2) Done
# 3)
class grandfater:
    def __init__(self,name , job):
        self.name = name
        self.job = job
    def home(self):
        print("Rented")


class father(grandfater):
    def __init__(self, name, job):
        super().__init__(name, job)
        self.skill = 'gradening'
    def home(self):
        print("Owned")

class mother:
    def __init__(self , name , job):
        self.name = name
        self.job = job
        self.skill = 'Cooking'

class child1(father, mother):
    def __init__(self, name, job):
        super().__init__(name, job)

# Applying MRO for Solving the 5 numbers Question
class child2(mother, father):
    def __init__(self, name, job):
        super().__init__(name, job)

# # 3) wher child2 lives
# c2 = child2('Ronok', 'programmer')
# c2.home()

# To solve 5 Number Quesiton
c1 = child1('jira', 'Bekar')
c1.home()
print(c1.__dict__)

c2 = child2('rafi', 'chagol seller')
c2.home()
print(c2.__dict__)
