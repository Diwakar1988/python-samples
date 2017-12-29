#FOR LOOP
print("#for: with loop variable")
# i will be initialized with min value (i.e. 0 here ) lessthan max value (i.e. 1 in this case)
for i in range(0,2):
    print(i)

print("\n#for: iterating on a list")
people = ["Jac","Bob","Lee"]

#for-each
print("\t*** for-each ***")
for person in people:
    print("\tName:",person)
print("\n\t*** for in range ***")
for i in range (0,len(people)):
    print("\tName:",people[i])

#WHILE LOOP
print("\n# while: with loop variable")
count=0
while count!=5:
    print("count",count)
    count+=1
    if count==3:
        break