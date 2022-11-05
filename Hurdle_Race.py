import math
import os
import random
import re
import sys

def hurdleRace(k, height):
    m = max(height)
    count = m-k
    if count<=0:
        return 0
    else:
        return count 