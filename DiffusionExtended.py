#William Taing CSS 458

#Preconditions: lat is a grid
#Postconditions: lat has changed due to diffusion
def applyDiffusionExtended(m, n, latExt):
    #Create lat, a lattice of latExt wihout the extended boundaries
    lat = [[]]
    
    for i in range(1, m):
        for j in range(1,n):
            lat[i-1][j-1].append(diffusion(diffusionRate, latExt[i][j],\
            latExt[i-1][j], latExt[i-1][j+1], latExt[i][j+1], latExt[i+1][j+1],\
            latExt[i+1][j], latExt[i+1][j-1], latExt[i][j-1], latExt[i-1][j-1])      
    return lat
            
