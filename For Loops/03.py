def generateNumber(start,end,step):
    if step>0:
        return range(start,end+1,step)
    else: 
        return range(start,end,step)