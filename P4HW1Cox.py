#cti 110
# P4HW1 Grade List
#Leo Cox
#11/1/22

#Ask for 6 grades for 6 modules 

grades = []


for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)

print("The grades are: ", grades)

# max and min

print ("Highest grade: ", max(grades))

print ("Lowest grade: ", min(grades))

#total and average

total = sum(grades)
count = len(grades)
average = total/count

print ("Total is: ", total)
print("Average is: ", average)
