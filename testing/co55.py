


import numpy


l = numpy.zeros((2,),)
l[0] = 1.09835073296562E-05
l[1] = 1.00456360209651E-06


n = numpy.zeros((3,),)
n[0] = 10.0
n[1] = 0.0
n[2] = 0.0

loss = numpy.zeros((2,),)
loss[0] = 0.0
loss[1] = 0.0

tend = 6000
t = 0.0
dt = 0.001
while(t<tend):
  loss[0] = n[0] - n[0] * numpy.exp(-l[0] * dt)
  loss[1] = n[1] - n[1] * numpy.exp(-l[1] * dt) 

  n[0] = n[0] - loss[0]
  n[1] = n[1] + loss[0] - loss[1]
  n[2] = n[2] + loss[1]
  
  t = t + dt
print(n)
