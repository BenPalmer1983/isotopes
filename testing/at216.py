


import numpy


l = numpy.zeros((3,),)
l[0] = 2310.4906018664847
l[1] = 0.0001907919572144083
l[2] = 0.0037839675759359388


#['At', 216, None, None, 0][83, 212, 1.0, 2310.4906018664847, 0][81, 208, 0.3594, 0.0001907919572144083, 1][82, 208, 1.0, 0.0037839675759359388, 1]


n = numpy.zeros((4,),)
n[0] = 10.0
n[1] = 0.0
n[2] = 0.0
n[3] = 0.0

loss = numpy.zeros((3,),)
loss[0] = 0.0
loss[1] = 0.0

steps = 1000000
tend = 1.0
t = 0.0
dt = tend / steps
while(t<tend):
  loss[0] = n[0] - n[0] * numpy.exp(-l[0] * dt)
  loss[1] = n[1] - n[1] * numpy.exp(-l[1] * dt) 
  loss[2] = n[2] - n[2] * numpy.exp(-l[2] * dt) 

  n[0] = n[0] - loss[0]
  n[1] = n[1] + loss[0] - loss[1]
  n[2] = n[2] + 0.3594 * loss[1] - loss[2]
  n[3] = n[3] + loss[2]
  
  t = t + dt
print(n)
