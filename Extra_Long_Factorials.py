import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    if n>=1:
        return(n*extraLongFactorials(n-1))
    else:
        return 1