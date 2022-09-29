def countApplesAndOranges(s, t, a, b, apples, oranges):
    totala = totalb = 0
    for i in range(len(apples)):
        if s<= a+apples[i] <= t:
            totala = totala+1
    for i in range(len(oranges)):
        if s<= b+oranges[i] <= t:
            totalb = totalb+1
    return(totala, totalb)

