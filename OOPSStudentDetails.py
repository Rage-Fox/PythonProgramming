class Student():
    def __init__(self,name,roll,m1,m2):
        self.name=name
        self.roll=roll
        self.m1=m1
        self.m2=m2
    def display(self):
        print("Name:",self.name)
        print("Roll Number:",self.roll)
    def printf(self):
        print("Subject 1 Marks:",self.m1)
        print("Subject 2 Marks:",self.m2)
    def avg(self):
        print("Average is:",(self.m1+self.m2)/2)
a=Student(input(),input(),int(input()),int(input()))
a.display()
a.printf()
a.avg()
