'''
3) Implemented that grandfather has rented house , father owned one , and show child2 where lived
'''

class GrandFather:
    def __init__(self):
        self.rented_house = 'Rented House'

class Father(GrandFather):
    def __init__(self):
        super().__init__()
        self.house = 'Owned House'  

class Child2(Father):
    def __init__(self):
        super().__init__()
    def show(self):
        print(f"Child2 lives in {self.house}")

# Creating Object of Child2
child2_object = Child2()

child2_object.show()
