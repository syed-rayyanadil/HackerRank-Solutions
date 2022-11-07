import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    return (max(set(arr), key = arr.count))