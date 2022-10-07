import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    alpha = []
    val = []
    y = word.upper()
    print(y)
    # pos = ord(y[1])-64
    # print(pos)
    for i in y:
        alpha.append(ord(i)-64) 
    print ("this is alpha",alpha[0])
    
    for j in range (len(alpha)):
        # print(h[j])
        z = alpha[j] 
        x= h[z-1]
        print("this is place",x)
        val.append(x)                
        
    tallest = max(val)
    count = len(word)
    print(tallest, count)
    
    return(tallest*count)