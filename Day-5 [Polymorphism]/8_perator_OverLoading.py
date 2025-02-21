class student :
    def __init__(self, m1 , m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1, m2)
        return s3

    def __str__(self):
        return self.m1 , self.m2



# Creating Two objects for this classes
s1 = student(40, 60)
s2 = student(90, 40)


'''
When you call a object behind the scene this wil call a String,
even , if we don't call it, it is happening behind the scene
'''
# # this will show the addres of s1
# print(s1)

# Method Overloading is already Happend here czz By default it's sting
'So if i dont define the Str funciton , this print the Module Name '
print(s1.__str__())
