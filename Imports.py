'''
TIPS:
1. We can import all variable and function in single statement i.e. import <module_name>. This <module_name> will act as a public object which can access all members of Greet module
2. Import (import)can be used anywhere before using module's member but as a good practice we should use import statements at one place(first line of the program)
'''
# imports all things of the Greet module/file
import Greet
Greet.sayBye("Diwakar") #calling function with object Greet that we've imported

# imports only sayHello function of the Greet module/file
from Greet import sayHello
sayHello("Diwakar") #calling function without object Greet(Optional) that we've imported

