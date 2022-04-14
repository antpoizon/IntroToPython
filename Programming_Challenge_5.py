# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:33:40 2022

@author: Ryan Borowski
"""

def FallingDistance(time_in_fall):
    counter = 1
    for x in range(0, time_in_fall, 1):
        distance_fallen = counter ** 2
        distance_fallen *= 9.8 * 0.5
        print(f"The object fell {distance_fallen} in {counter} seconds.")
        counter += 1
        return distance_fallen
        

def main():
    print('Hello! Welcome to my freefall calculator.\n')
    time_in_fall = int(input("How long do you want to calculate the object falling for?\n"))
    FallingDistance(time_in_fall)






if __name__ == '__main__':
    main()