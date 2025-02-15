'''
2) Give everyone a name and Job attribute , But it can be declared at most 2 time .
Figure out where they should be (jobs : farmer , banker , artist , Teacher , Programmer )

'''
class GrandFather:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def show(self):
        print(f"GrandFather: {grandfather.name}, Job: {grandfather.job}")

class Father(GrandFather):
    def __init__(self, name, job):
        super().__init__(name, job)
    def show(self):
        print(f"Father: {father.name}, Job: {father.job}")

# I used Object in Mother class , czz instnaly amk root a back korte hobe
class Mother(object):
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def show(self):
        print(f"Mother: {mother.name}, Job: {mother.job}")

class Child1(Mother, Father):
    def __init__(self, name, mother_name, mother_job, father_name, father_job):
        Mother.__init__(self, mother_name, mother_job)
        Father.__init__(self, father_name, father_job)
        self.name = name
    def show(self):
        print(f"Child1: {child1.name}, Father: {child1.name}, Mother: {child1.name}")


class Child2(Mother, Father):
    def __init__(self, name, mother_name, mother_job, father_name, father_job):
        Mother.__init__(self, mother_name, mother_job)
        Father.__init__(self, father_name, father_job)
        self.name = name
    def show(self):
        print(f"Child2: {child2.name}, Father: {child2.name}, Mother: {child2.name}")

# Creating objects with names and jobs
grandfather = GrandFather("Banker er Bap", "Farmer")
father = Father("Ronoker er Bap", "Banker")
mother = Mother("Ronoker er Ma", "Artist")
child1 = Child1("Ronoker Er boro Bhai", "Ronoker er Ma", "Artist", "Ronoker er Bap", "Banker")
child2 = Child2("Ronok", "Ronoker er Ma", "Artist", "Ronoker er Bap", "Banker")

# For Ronok er Dada
grandfather.show()
# For ronok er Bap
father.show()
# For Ronoker Ma
mother.show()
# for Ronoker er Bhai
child1.show()
# For amr bondhuu Ronok
child2.show()