# TIP: Python may have instance variable without declaration

class Person:
    pay=1.2
    salary=0.0
    def raisePay(self):
        self.salary = self.salary* self.pay

diwakar = Person()
diwakar.fname = "diwakar" # instance variable not a class variable
diwakar.lname = "mishra"
diwakar.salary = 1000
print(diwakar.__dict__) # used to get key value pair of class/instance variable, key=variable name and value=current value

danny = Person()
danny.fname = "Danny"
danny.lname = "Dude"
danny.salary = 500
print("Before raise",danny.__dict__)
danny.raisePay()
print("After raise",danny.__dict__)