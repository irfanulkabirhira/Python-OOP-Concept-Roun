
# Method Over-ridding--> Def fley k ==> override korci
class bird:
    def fly(self):
        print("Bird is Flying")

class Aroplane:
    def fly(self):
        print("Aroplane is Flying")

def display(obj):
    obj.fly()


duel = bird()
Emirates = Aroplane()

duel.fly()
Emirates.fly()