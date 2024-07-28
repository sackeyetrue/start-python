# Examination Grading Program
import random
print("Examination Grade System:")

studentName = input("Enter Your Name: ")
studentMark = 87 #random.randrange(1,100)
grades = ["A","B","C","D","E","F"]

def gradingScheme():
    if studentMark >= 80 :
        return (f"Student Name: {studentName}\nMark: {studentMark}\nGrade: {grades[0]}")
    else :
        return "Error"


getGrade = gradingScheme()
print(getGrade)