import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    list2 = []
    arr.sort()
    # print(arr)
    x = sum(arr[1:])
    y = sum(arr[:-1])
    print(y, x)