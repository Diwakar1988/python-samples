myStr= "Hello World!"

print("myStr = ",myStr)

#calculate string length
print("len(myStr) = ",len(myStr))

#search a sub string, find() function returns index number if sub string found in main string otherwise -1
print('''myStr.find("l") = ''',myStr.find("l"))
print('''myStr.rfind("l") = ''',myStr.rfind("l"))

#search a sub string, index() function returns index number if sub string found in main string otherwise exception
print('''myStr.index("l") = ''',myStr.index("l"))
print('''myStr.rindex("l") = ''',myStr.rindex("l"))


#make the first character have upper case and the rest lower case.
print("myStr.capitalize() = ",myStr.capitalize())

#swap case of characters
print("myStr.swapcase() = ",myStr.swapcase())

#count char
sub="l"
print("myStr.count(sub) = ",myStr.count(sub))

#replace string
print('''myStr.replace("World","Everyone") = ''',myStr.replace("World","Everyone"))

#check string starts with (its a case sensitive function)
print('''myStr.startswith("Hello") = ''',myStr.startswith("Hello"))
print('''myStr.startswith("hello") = ''',myStr.startswith("hello"))

#check string ends with (its a case sensitive function)
print('''myStr.endswith("World!") = ''',myStr.endswith("World!"))

# split into list
print("myStr.split() = ",myStr.split())
print("myStr.split('l') = ",myStr.split("l"))
print("myStr.split('l',2) = ",myStr.split("l",2))