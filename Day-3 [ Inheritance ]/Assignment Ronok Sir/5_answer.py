# 5) lastly , show child1's and child2's  details


class GrandFather:
    def __init__(self, name, job):
        self.name = name
        self.job = job

class Father(GrandFather):
    def __init__(self, name, job):
        super().__init__(name, job)

class Mother:
    def __init__(self, name, job):
        self.name = name
        self.job = job

class Child1(Mother):
    def __init__(self, name, mother_name, mother_job):
        super().__init__(mother_name, mother_job)
        self.name = name
        self.job = mother_job

    def show(self):
        print(f"Child1: {self.name}, Job is: {self.job}")

class Child2(Father, Mother):
    def __init__(self, name, father_name, father_job):
        Father.__init__(self, father_name, father_job)
        self.name = name
        self.job = father_job

    def show(self):
        print(f"Child2: {self.name}, Works as: {self.job}")

child1 = Child1("Ronoker Er Boro Bhai", "Mother Name", "Gareden")
child2 = Child2("Ronok", "Father Name", "Kitchen")

child1.show()
child2.show()
