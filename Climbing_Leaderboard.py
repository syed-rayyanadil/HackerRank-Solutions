import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked  = list(set(ranked))
    ranked.sort()
    n = len(ranked)
    result = []
    i=0
    for alscore in player:
        while i<n and ranked[i]<=alscore:
            i+=1
        result.append(n-i+1)
    return(result)