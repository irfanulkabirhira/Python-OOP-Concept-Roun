# if Both class assign the same number of paramiters , then we we will call that constractor over-riding

class father:
    def __init__(self, name , work):
        self.name = name
        self.work = work
    def show(self):
        print(f"Father's name is : {self.name} , and Work is : {self.work}")

class son(father):
    #Mehtod over-riding
    def __init__(self, name, gf):
        self.name=name
        self.gf = gf
        self.work = 'Programmer'
    def show(self):
        print(f"name : {self.name} , work is : {self.work} And  GF is : {self.gf}")

s = son('Hira','GF')
s.show()