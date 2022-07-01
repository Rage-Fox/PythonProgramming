#acquiring properties of a class is called inheritance
#Inheritance needs two classes(parent and child)
class Person():
    college='Aditya'
    def __init__(self,name,aadhar,college):
        self.name=name
        self.aadhar=aadhar
        #self.college=college
    def display(self):
        print(self.name,self.aadhar,self.college)
class Student(Person):#child class acquiring properties from parent class
    #college='AEC'
    def __init__(self,name,aadhar,rollno,college):
        self.rollno=rollno#instance variable
        #self.college=college
        super().__init__(name,aadhar,college)#this makes variables access from parent Person() class
        #we can access instance variable from parent class without even calling it!
        #college variable order as: chils instance>class variable>parent instance>parent variable
    def display(self):
        print(self.name,self.aadhar,self.rollno,self.college)
a=Student('Harsha',795862070077,'21A91A05G6','aec')
a.display()
