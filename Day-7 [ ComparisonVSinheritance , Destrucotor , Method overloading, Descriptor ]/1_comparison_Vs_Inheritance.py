'Comparison Vs Inheritance '
class Engine:
    def __init__(self , cc):
        self.capactity = cc
    def start(self):
        print("Engine is Started ")
    def stopped(self):
        print("Engine is stopped")


class Car(Engine):
    def __init__(self, cc , name):
        super().__init__(cc)
        self.name = name
    def run(self):
        print ("Car is Running")

c1 = Car(2000, "BMW")
c1.start()
c1.run()
c1.stopped()

'''
So . is this Actually Logical ??? How is this possoble that car is inherited from Engine ???
Comparison (has a engine ) --> to implement this , we wont't inherited Engine in Car Class
Inheritance(is a ) -->
No right !!!

'''
