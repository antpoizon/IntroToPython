# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:31:45 2022

@author: Ryan Borowski
"""
def FileControl():
    readFile = open('C:\\Users\\Ryan Borowski\\Desktop\\FunWithFiles.txt', 'r')
    lineOne = readFile.readline()
    lineTwo = readFile.readline()
    lineThree = readFile.readline()
    print(f'{lineOne}\n{lineTwo}\n{lineThree}')
    userMovie = str(input("What is the title of your favorite movie?"))
    readFile.close()
    addMovie = open('C:\\Users\\Ryan Borowski\\Desktop\\FunWithFiles.txt', 'a')
    addMovie.write('\n' + userMovie)
    addMovie.close()
    



def main():
    FileControl()


if __name__ == '__main__':
    main()