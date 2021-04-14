

# make a new instance of class called Students
class Student(object):
    # initialse the instance with the following attributes
    def __init__(self, first_name,last_name, undergraduate_programme):
        # define all the parameters
        self.first_name= first_name
        self.last_name= last_name
        self.undergraduate_programme= undergraduate_programme
    # make a new function to write the name and the undergraduate programme
    def example(self):
        return('Your name:'+self.last_name+' '+self.first_name+'  '+'undergraduate programme:'+self.undergraduate_programme)
# an example
a = "Yuyanran"
b = "Xu"
c = "BMS"
X = Student(a,b,c)
print(X.example())

# input your full name and your undergraduate programme
first_name = input("Your first name:")
last_name = input("Your last name:")
undergraduate_programme =input("Your undergraduate programme:")
X = Student(a,b,c)
print(X.example())

