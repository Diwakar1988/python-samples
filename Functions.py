'''
Key notes:
1. Scope of functions are defined by indent not by braces({})
2. Functions should be declared before using
3. Functions can have a default value in parameters, default value will be used when there is no value passed to function parameter
4. Functions can be called by value and reference 
'''

#declare a function

### Function with no argument no return value
def printMyDOB():
    print("17-Jul-1988")

### Function with no argument but return value
def getDOB():
    return "17-Jul-1988"

### Function with argument no return value
def makeDOB(dd=17,mm="-Jul-",yy=1988):
    dob = str(dd)+mm+str(yy)
    return dob
    
### Function with argument with return value
def add(a,b):
    return a+b

def addItemInList(personList,person="Person"):
    personList.append(person)
#calling a function

printMyDOB()
print(getDOB())
print(makeDOB())
print(makeDOB(6,"-May-",1989))
print(add(10, 6)) #call by vale

#call by reference
personList = ["Jack","Mac"]
print(personList)
addItemInList(personList, "Diwakar")
print(personList)