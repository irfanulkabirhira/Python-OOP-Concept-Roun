class father:
    def __init__(self, name , work):
        self.name = name
        self.work = work
        self.home = 'Owned'
    def show(self):
        print(f"name is :{self.name} , age is :{self.work}")

    def setName (self , name):
        self.name = name


class son(father):
    def __init__(self, name, gf):
        super().setName(name)
        self.gf = gf


        def show(self):
            print(f"name is :{self.name} , age is :{self.work} , and GF is : {self.gf}")

S = son('Hira', 'Barsha')
print(S.__dict__)

