import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    l0  = []
    lp = []
    ln = []
    for i in range (n):
        if(arr[i]==0):
            l0.append(arr[i])
        elif (arr[i]<0):
            ln.append(arr[i])
        elif(arr[i]>0):
            lp.append(arr[i])
            
    z = len(l0)/n
    p = len(lp)/n
    n2 = len(ln)/n
    
    return(p, n2, z)