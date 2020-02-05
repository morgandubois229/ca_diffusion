#==============================================================================
# Grid plot demo
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N
import matplotlib
import matplotlib.pyplot as plt


#- Preliminaries:

length = 42
width = 42
data = N.ones((length, width, 3), dtype='f')*0.8


#- Create figure and axes:

fig = plt.figure(figsize=(5,5))
#ax = fig.add_axes( (0.0, 0.0, 1.0, 1.0), frameon=False )
ax = fig.add_axes( (0.4, 0.3, 0.2, 0.4), frameon=False )


#- Set first display data values:

data[20,18,:] = N.array([1, 0, 0])

colorit = matplotlib.colors.colorConverter.to_rgb('b')
data[10,8,:] = colorit[:]


#- Draw first image:

img = ax.imshow(data, interpolation='none',
                extent=[0, width, 0, length],
                aspect="auto",
                zorder=0)
ax.axis('off')
plt.draw()

plt.pause(2)


#- Change data some for second image to display:

data[20,18,:] = matplotlib.colors.colorConverter.to_rgb('y')
data[3,2,:] = N.array([1,1,1])


#- Draw second image:

img.set_data(data)
plt.draw()




#===== end file =====
