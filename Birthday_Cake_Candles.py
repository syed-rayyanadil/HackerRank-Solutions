import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    x = max(candles)
    count = 0
    for i in range(len(candles)):
        if (candles[i] == x):
            count = count+1
    return (count)