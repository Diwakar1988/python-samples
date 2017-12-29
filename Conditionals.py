'''
REMEMBER??
1. if-else block scope is determined by indentation/alignment not by '{}' (parenthisis) 
2. condition results should be either 'True' or 'False' constants
3. Any numeric value (positive/nigative), will be considered as 'True' condition
'''

num = 10
color= "red"
print("num=",num," color=",color)

#SIMPLE IF
print("\n#Simple if")
if 1.5:
    print("num is equals to 10")
    print("with indent","num==10") #this print() is part of if block since its align to above statement
print("without indent","num==10") #this print() is not a part of if block since its not aligned to above statement

#SIMPLE IF-ELSE
print("\n#Simple if-else")
if num==10:
    print("num is equals to 10")
else:
    print("num is no equals to 10")
    
#SIMPLE LIF (IF-ELSE-IF) 
print("\n#Simple elif (if-else-if)")

if color=='red':
    print("color is RED")
elif color=='blue':
    print("color is BLUE")
else:
    print("color is not RED or BLUE")
