class student:
    #this init method is called Dender in python
    # Constractor
    def __init__(self, my_roll, my_name , my_marks):
        # this are attribite where roll, name , marks are variables
        self.roll = my_roll
        self.name = my_name
        self.marks = my_marks

        # An Action Method
    def avargae(self):
        return sum(self.marks)/len(self.marks)

# Creasting object of this class
first_student = student(1,'Hira', [50, 60 , 70 , 80])
print(first_student.name)
print("This avarge marks of hira is = ",first_student.avargae())



