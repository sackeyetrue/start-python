# Examination Grading Program
import random
print("Examination Grade System:")

studentName = input("Enter Your Name: ")
studentMark = random.randrange(1,100)
grades = ["A","B","C","D","E","F"]

def gradingScheme():
    if studentMark >= 80 :
        return (f"Student Name: {studentName}\nMark: {studentMark}\nGrade: {grades[0]}")
    elif studentMark >= 70 :
        return (f"Student Name: {studentName}\nMark: {studentMark}\nGrade: {grades[1]}")
    elif studentMark >= 60 :
        return (f"Student Name: {studentName}\nMark: {studentMark}\nGrade: {grades[2]}")
    elif studentMark >= 50 :
        return (f"Student Name: {studentName}\nMark: {studentMark}\nGrade: {grades[3]}")
    elif studentMark >= 40 :
        return (f"Student Name: {studentName}\nMark: {studentMark}\nGrade: {grades[4]}")
    elif studentMark <= 30 :
        return (f"Student Name: {studentName}\nMark: {studentMark}\nGrade: {grades[5]}")
    else :
        return "Error"


getGrade = gradingScheme()
print(getGrade)