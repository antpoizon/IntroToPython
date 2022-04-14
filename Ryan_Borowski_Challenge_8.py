# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:01:30 2022

@author: Ryan Borowski
"""
# This program takes an inputted user password, and checks it against multiple criteria
# These criteria include checking against the 50 most common passwords, checking for upper and lowercase,
# checking for a length of at least 8 characters, checking for a number, checking for symbols from a predetermined list,
# and checking for unallowed symbols. Each of these checks are designated to a different function

# The general logical structure of this script is to ask for a password, call each checker function, and if it passes the check,
# it returns to try the next checker function. If it does not pass, the checker functions call the getUserPass() function to force a new password,
# and ensure that all criteria are tested for each new password

passDatabase = []
#takes the password value passed to it, adds \n to the end of it, then checks the passDatabase list against the new password string (with \n), and then passes a list back to getUserPass
def StoredPasswords(checkPass):
    global passDatabase
    found = 'Your password is too weak'
    with open('C:\\Users\\Ryan Borowski\\Desktop\\50_Common_Passwords.txt') as commonPasswords:
        passDatabase = commonPasswords.readlines()
    passwordToCheck = checkPass + '\n'
#    print(passwordToCheck)
    if passwordToCheck in passDatabase:
        indexOfPassword = [str(passDatabase.index(passwordToCheck)) + ' is the value of the index which your pasword is located on the common password list \n']
        foundResponse = found + indexOfPassword
        print(foundResponse)
        getUserPass()
    elif passwordToCheck not in passDatabase:
        return 'Your password is strong enough to not be found in the 50 most common passwords. Good job! \n'
    
    
        
# gets the username and password from the user, and calls each password checker function one-by-one
# gets re-called each time an unacceptable password is detected, to force a new password from the user
def getUserPass():
    global passDatabase
    username = str(input("Please enter a Username\n"))
    print(f"{username} is a great username! If this line doesn't exist, spyder gets annoyed that i declare then dont use a variable, and I'm tired of looking at that tiny triangle \n")
    password = str(input('Please enter a password with at least 8 characters, a number, a capital letter, one lowercase letter, and one special character: !@%^&*(), password cannot contain #$_-+= \n'))
    result = lengthChecker(password)
    print(result)
    result = hasNumber(password)
    print(result)
    result = upperAndLowerChecker(password)
    print(result)
    result = symbolChecker(password)
    print(result)
    result = StoredPasswords(password)
    print(result)
    print('Your password meets all of the requirements! Adding password to database now \n')
    passDatabase.append(password)
#    print(passDatabase[-1])
#    print(passDatabase)

# accepts an argument of the attempted password, and then checks counts the characters in the password with charCounter
# if password is too short, prints a statement, and then calls getUserPass() again to ensure the user must enter a new password
def lengthChecker(userPass):
    charCounter = 0
    for ch in userPass:
        charCounter += 1
    if charCounter >= 8:
        return "Password is an acceptable length. \n"
        
    elif charCounter <= 8:
        print("Password is too short. Password must be at least 8 characters \n")
        getUserPass()
# defines 2 seperate variables for upper and lowercase, and checks both with an 'and' statement to ensure password has both uppercase and lowecase
# if it fails to have EITHER an uppercase OR a lowercase, returns a string explanation and calls getUserPass() again to ensure user must choose new password
def upperAndLowerChecker(userPass):
    upperCheck = 0
    lowerCheck = 0
    for ch in userPass:
        if ch.isupper() == True:
            upperCheck += 1
        if ch.islower() == True:
            lowerCheck += 1
    if upperCheck and lowerCheck >= 1:
        return "Password satisfies upper and lowercase requirements. Good job! \n"
    elif upperCheck or lowerCheck < 1:
        print("Your password requires at least 1 uppercase and 1 lowercase letter. Please choose a new password \n")
        getUserPass()

# uses a for loop to check each character in the password for a number, then uses if/elif to return a decision
# if password does not have a number in it, re-calls getUserPass() to force a new password selection
def hasNumber(userPass):
    numOfDigits = 0
    for ch in userPass:
#        print(ch)
#        print(ch.isdigit())
        if ch.isdigit() == True:
            numOfDigits += 1
#            print(numOfDigits)
    if numOfDigits == 0:
        print('There are no numbers contained in your password. Please choose a password with atleast 1 number \n')
        getUserPass()
    elif numOfDigits >= 0:
        return f'Your password contains {numOfDigits} numbers, which satisfies the condition of at least 1 number. Good Job! \n'
# uses 2 strings to store unallowed and required symbols, and 2 int variables to store each instance of a bad symbol or good symbol being used

# uses a for loop and in operator to check each character individually, and then a decision structure following the for loop 
# to decide whether the password meets symbol requirements, or whether to call getUserPass() and force a new password
def symbolChecker(userPass):
    reqSymbols = '!@%^&*()'
    noGoSymbols = '#$_-+='
    goodSymbols = 0
    badSymbols = 0
    for ch in userPass:
        if ch in reqSymbols:
            goodSymbols += 1
        elif ch in noGoSymbols:
            badSymbols += 1
    if goodSymbols < 1 or badSymbols >= 1:
        print(f"Your password fails to contain any symbols from the list: {reqSymbols}, or uses unallowed symbols like {noGoSymbols} \n")
        getUserPass()
    elif goodSymbols >= 1 and badSymbols < 1:
        return "Your password may complies with symbol rules. Good Job! \n"
    

if __name__ == '__main__':
    getUserPass()
    

        