#basic structure of a class
#there are no actual and formal parameters in OOPS, all are just parameters
#create a class with the first letter as capital
class Car():
    #if you create an object, the constructor will be executed without even calling it
    def __init__(self,name,model):#constructor
        #self is nothing but a parameter of the particular object(a,b,....) or object of a particular instance
        pass#doesn't execute or it will just pass
        self.name=name#instance variables or local variables
        self.model=model#instance variables or local variables
        print("My favourite car")
    #instance methods
    #this will not executes unless it is being called
    def display(self):
        print(self.name,self.model)
a=Car('Lamborghini','Spider')#object
a.display()
print(a.name)#we can access instance variable outside of the object class too..
b=Car('Range Rover','Land Rover')
b.display()
