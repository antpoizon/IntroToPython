# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:08:03 2022

@author: Ryan Borowski
"""
# Challenge 9

gradebookDict = {}

def Menu():
    choice = input("Would you like to add a student to the gradebook? Enter y or n")
    if choice.upper() == 'Y':
        addStudent()
    elif choice.upper() == 'N':
        print ('you got it')
        print("Your gradebook is as follows")
        print(gradebookDict)

def addStudent():
    stuName = input('Please enter the name of the student to add')
    gradeValue = []
    for grades in range(0,3):
        print(grades)
        stuGrade = str(input(f"Please enter grade {grades} to add"))
        gradeValue.append(stuGrade)
    StudentGradebook(stuName, gradeValue)

def StudentGradebook(name, grade_value):
    global gradebookDict
    gradebookDict[name] = grade_value
    print(gradebookDict[name])
    Menu()
if __name__ =='__main__':
    Menu()