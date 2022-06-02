class Student():
    college='Aditya'#class/static
    #we can use this static anywhere without even getting that to input by the user
    def __init__(self,name,roll,m1,m2,college):
        self.name=name
        self.roll=roll
        self.m1=m1
        self.m2=m2
        self.college=college
    def display(self):
        print("Name:",self.name)
        print("Roll Number:",self.roll)
        print("College:",self.college)
    def printf(self):
        print("Subject 1 Marks:",self.m1)
        print("Subject 2 Marks:",self.m2)
    def avg(self):
        print("Average is:",(self.m1+self.m2)/2)
a=Student(input(),input(),int(input()),int(input()),input())#if college is given here as instance variable, i'll have more priority than the class college variable
a.display()
a.printf()
a.avg()
#to call something outside of the object, do a.m1, a.m2, etc....
