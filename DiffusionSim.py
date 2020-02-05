#William Taing CSS 458

#Preconditions: m is amount of rows, n is amount of columns, t is time steps
#               diffusionRate is a constant
#Postconditions:
def diffusionSim(m, n, diffusionRate, t):
    bar = initBar(m, n, hotSites, coldSites)
    grids = []
    grids.append(bar)
    for i in range(t):
        barExtend = reflectingLat(bar)
        bar = applyDiffusionExtended(m, n, diffusionRate, barExtended)
        bar = applyHotCold(bar, hotSites, coldSite)
        grids.append(bar)
    return grids
