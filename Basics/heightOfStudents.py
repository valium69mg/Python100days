''' 
THIS PROGRAM CALCULATES THE AVERAGE HEIGHT OF A GROUP OF STUDENTS
DATE: 27.09.2023
AUTHOR: CARLOS TRANQUILINO CARLOS ROMAN
'''
from random import randint

heightOfStudents = []
sumOfHeights = 0
numberOfStudents = 0

for student in range(0,20): #20 STUDENTS HEIGHTS GENERATED RANDOMLY
    height = randint(150,190)
    heightOfStudents.append(height)

for i in heightOfStudents:
    numberOfStudents += 1

for i in range(0,numberOfStudents): #SUM ALL THE HEIGHTS OF THE STUDENTS
    sumOfHeights += heightOfStudents[i]

averageHeight = round(sumOfHeights/(numberOfStudents)) # DEFINE THE AVERAGE 
    
# PRINT THE HEIGHTS AND AVG HEIGHT
print("Heights of Students: {}".format(heightOfStudents))
print("Average Height of a Student: {} cm".format(averageHeight))

