class student :
    def __init__(self, m1 , m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1, m2)
        return s3



# Creating Two objects for this classes
s1 = student(40, 60)
s2 = student(90, 40)
s3 = student(30, 20)

s4 = s1 + s2 +s3
print(s4.m1)
print(s4.m2)


