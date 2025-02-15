# # Multi-Level Inheritance ==> it's obviously a flow -> Granffather-> father-> son

"""
class grand_father:
    pass
# Intermediate Class 1 - inheriting from grand_father
class father(grand_father):
    pass

# Intermediate Class 2 - inheriting father
class son(father):
    pass

"""

class grand_father:
    def __init__(self):
        print("Grandfather initialized")

class father(grand_father):
    def __init__(self):
        super().__init__()
        print("Father initialized")

class son(father):
    def __init__(self):
        super().__init__()
        print("Son initialized")

# Create an object to see the output
obj = son()
