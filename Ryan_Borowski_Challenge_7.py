# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:01:30 2022

@author: Ryan Borowski
"""
#takes the password value passed to it, adds \n to the end of it, then checks the passDatabase list against the new password string (with \n), and then passes a list back to getUserPass
def StoredPasswords(checkPass):
    found = ['Your password is too weak']
    notFound = 'Your password is strong enough to not be found in the 50 most common passwords. Good job!'
    commonPasswords = open('C:\\Users\\Ryan Borowski\\Desktop\\50_Common_Passwords.txt')
    passDatabase = commonPasswords.readlines()
    commonPasswords.close()
    passwordToCheck = checkPass + '\n'
    #print(passwordToCheck)
    if passwordToCheck in passDatabase:
        indexOfPassword = [str(passDatabase.index(passwordToCheck)) + ' is the value of the index which your pasword is located on the common password list']
        foundResponse = found + indexOfPassword
        #print(foundResponse)
        return foundResponse
    elif passwordToCheck not in passDatabase:
        return notFound
    
    
        
#gets the username and password from the user, and calls the stored password function
def getUserPass():
    username = str(input("Please enter a Username\n"))
    print(f"{username} is a great username! If this line doesn't exist, spyder gets annoyed that i declare then dont use a variable, and I'm tired of looking at that tiny triangle")
    password = str(input('Please enter a password\n'))
    lengthChecker(password)
    result = StoredPasswords(password)
    #used to check if the value that was returned is in list form or string form, which is an easy way to check whether the password was found or not when printing out the response statements
    if len(result) == 2:
        print(result[0])
        print(result[1])
    elif len(result) != 2:
        print(result)

def lengthChecker(userPass):
    charCounter = 0
    for ch in userPass:
        charCounter += 1
    if charCounter >= 8:
        print("Password is an acceptable length.")
    elif charCounter <= 8:
        print("Password is too short. Password must be at least 8 characters")
        getUserPass()




if __name__ == '__main__':
    getUserPass()
    

        