# Multi-Level Inheritance ==> it's obviously a flow -> Granffather-> father-> son
class grand_father:
    pass
class father(grand_father):
    pass
class son(father):
    pass