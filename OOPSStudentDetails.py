class Student():
    college='Aditya'#class/static
    #we can use this static anywhere without even getting that to input by the user
    def __init__(self,name,roll,m1,m2,college):
        self.name=name
        self.roll=roll
        self.m1=m1
        self.m2=m2
        self.college=college
    #instance methods has to be called with the help of self(object)
    def display(self):
        print("Name:",self.name)
        print("Roll Number:",self.roll)
        print("College:",self.college)
    def printf(self):
        print("Subject 1 Marks:",self.m1)
        print("Subject 2 Marks:",self.m2)
    def avg(self):
        print("Average is:",(self.m1+self.m2)/2)
    #classmethod is very strict with the variables
    @classmethod#which gives priority to class variables like college='aditya'
    def classm(cls):#have to give a default parameter
        print(cls.college)
        #without class variable IDLE Python shell shows--> AttributeError: type object 'Student' has no attribute 'college'
        #classmethod has the ability of changing the class variables
    #not as strict as classmethod and we don't need to give or pass any variables(object)
    @staticmethod
    def staticcm():
        print("Done!")
        #cannot change the class variables(objects)
        #we can also pass variables into this static method irrespective of the class variables and instances(something like an integer without self.integer)
a=Student(input(),input(),int(input()),int(input()),input())#if college is given here as instance variable, i'll have more priority than the class college variable
a.display()
a.printf()
a.avg()
a.classm()
Student.classm()#both do the same task
a.staticcm()
#to call something outside of the object, do a.m1, a.m2, etc....
'''
Harsha
21A91A05G6
99
100
AEC
'''
