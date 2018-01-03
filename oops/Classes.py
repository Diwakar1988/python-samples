'''
TIPS:
1. use class keyword to declare a class
2. '__' double underscore declares a private class member
3. __dict__ with object/class name tells about the object scehma in key-value fashion
4. Pass self as first argument whenever declaring function or __init__/constructor
5. If you declare a __init__/construtor then default  __init__/construtor will not be used
5. Python may have instance variable without declaration
'''
class Account:
    # class variables
    type=""
    limit=0.0
    
    # constructor
    def __init__(self,accountType,limit):
        self.type=accountType
        self.limit=limit
    
    # argument with default value
    def increaseLimitBy(self,amount=0.0):
        self.limit+=amount
        return self.limit
    
    def toString(self):
        return "Type={}, limit={}".format(self.type,self.limit)

# create an Account
saving = Account("Saving",100) # we can ommit self here, self will be automatically passed once you call class function
print(saving.toString()) #calling function without self
print(Account.toString(saving)) # calling function with self, both are same


current = Account("Current",1000)
print(current.toString())
print("current.increaseLimitBy(1000)",current.increaseLimitBy(1000))
print(current.toString())