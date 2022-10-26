import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    x=[]
    
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            a= ar[i]
            b = ar[j]
            if((a+b)%k == 0):
                x.append([a,b])

    return(len(x))         