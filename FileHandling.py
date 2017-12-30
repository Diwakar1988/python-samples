'''
TIPS:
1. File modes are r,r+,w(open an existing file to write),w+(create a file if not exist),a(append)
'''
#open an existing file
from time import time, strftime, gmtime
file = open("data.txt","r")

#file details/properties
print("File NAME: ",file.name)
print("File open MODE: ",file.mode)

#read a file
data = file.read()

print(data)

file.close();

#write on a file
file = open("data.txt","a")
file.write("\nWritten some text on "+strftime("%d-%m-%Y %H:%M:%S", gmtime()))
file.close();