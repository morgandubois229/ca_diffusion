
def reflectingLat(lat):
    shape = nu.shape(lat)
    relat = nu.zeros((shape[0]+2, shape[1]))
    
    relat[0, :] = lat[0, :]
    relat[1:shape[0]+1, :] = lat
    relat[shape[0]+1, :] = lat[shape[0]-1, :]
    return relat
