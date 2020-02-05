import numpy as N

AMBIENT = 25
HOT = 50
COLD = 0

def initBar(m, n, hotSites, coldSites):
    ambientBar = N.full((m, n), AMBIENT)
    return applyHotCold(ambientBar, hotSites, coldSites)
    
def applyHotCold(bar, hotSites, coldSites):
    newBar = bar
    for i in range(0, len(hotSites)):
        if ((i % 2) != 1):
            newBar[hotSites[i]][hotSites[i+1]] = HOT
    for i in range(0, len(coldSites)):
        if ((i % 2) != 1):
            newBar[coldSites[i]][coldSites[i+1]] = COLD
    return newBar