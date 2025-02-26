# Destructor
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
        # Has a comparison
        self.engine = Engine(cc)
    def run(self):
        self.engine.start()
        print ("Car is Running")
        self.engine.stopped()

c1 = Car(2000, "BMW")
c1.run()

del c1
c1.run()

"Now this won't Run anymore "