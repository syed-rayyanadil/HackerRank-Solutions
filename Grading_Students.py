import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here   
    x= 0     
    for i in range(len(grades)):
        if (grades[i]>=38):
            # print(grades[i])
            x = (math.ceil(grades[i]/5)*5)
            if (abs(grades[i]-x)<3):
                print(x)
                grades[i] = x                
            else: 
                print(grades[i])
        else:
            print(grades[i])
    return(grades)