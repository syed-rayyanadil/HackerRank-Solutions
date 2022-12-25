import math
import os
import random
import re
import sys

def organizingContainers(container):
    # print(n)
    r= [0]*n
    c= [0]*n
    for i in range (n):
        for j in range (n):
            r[i] =  r[i]+container[i][j]
            c[i] =  c[i]+container[j][i]
    if (sorted(r)==sorted(c)):
        return "Possible"
    else:
        return "Impossible"