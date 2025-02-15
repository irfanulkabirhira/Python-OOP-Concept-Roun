# Multi-Level Inheritance ==> it's obviously a flow -> Granffather-> father-> son
class grand_father:
    pass
# Intermediate Class 1 - inheriting from grand_father
class father(grand_father):
    pass

# Intermediate Class 2 - inheriting father
class son(father):
    pass