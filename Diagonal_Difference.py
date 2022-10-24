import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    l1 = []
    l2 = []
    n = len(arr)
    for i in range (n):
        for j in range (n):
            if (i == j):
                l1.append(arr[i][j])
            if ((i+j) == (n-1)):
                l2.append(arr[i][j])
    z = sum(l1)-sum(l2)
    return(abs(z))