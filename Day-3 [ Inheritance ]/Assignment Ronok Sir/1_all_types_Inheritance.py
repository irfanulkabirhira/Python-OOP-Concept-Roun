'''
Inheritance is 5 types
Single => single parent , single child
Hirarchical => Single parent  Multiple clases --> [office]
Multiple Inheritance => Multiple parents , single child
Multi-Level Inheritance =>Grandgater -> Father -> son

'''

# Single in heritance
class grand_father:
    pass
class father(grand_father):
    pass
# Multilevl Inheritance
class child1(father):
    pass
class mother(object):
    pass
# Multiple inheritance # same way this is also hierarchial
class child1(mother, father):
    pass
class child2(mother, father):
    pass

'''
As all applied so , this is Hybrid Inheritance as well
'''
