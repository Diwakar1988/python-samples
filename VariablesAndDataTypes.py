#DECLARE A VARIABLE
print("#DECLARE A VARIABLE")
num = 10
floatNum = 10.5
strName = "Diwakar Mishra"
listWeekDays=["S","M","T","W","T","F","S",7]
dictinaryMonthDays = {"Jan":31,"Feb":28,"Mar":31,"Apr":30,"May":31,"Jun":30,"Jul":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":30}

print(type(num),num)
print(type(floatNum),floatNum)
print(type(strName),strName)
print(type(listWeekDays),listWeekDays)
print(type(dictinaryMonthDays),dictinaryMonthDays)

#ACCESS LIST ELEMENTS
print("\n\n#ACCESS LIST ELEMENTS")
print("listWeekDays[1]",listWeekDays[1])
print("listWeekDays[0:2]",listWeekDays[0:2])
print("listWeekDays[0:listWeekDays.__len__()]",listWeekDays[0:listWeekDays.__len__()])

#ACCESS DICTIONARY ELEMENTS
print("\n\n#ACCESS DICTIONARY ELEMENTS")
print('''dictinaryMonthDays["Jan"]''',dictinaryMonthDays["Jan"])