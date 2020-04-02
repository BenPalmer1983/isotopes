import numpy



def activity(t, l, b, w, n0):
  nt = numpy.zeros((len(n0),),)
  for m in range(1,len(n0)):
    if(l[m] > 0.0):
      nt[m] = activity_unstable(t, l, b, w, n0, m)
    elif(l[m] == 0.0):
      nt[m] = activity_stable(t, l, b, w, n0, m)
  print(nt)

def activity_unstable(t, l, b, w, n0, m):
  s = 0.0
  for k in range(1, m+1):
    s = s + r(k, m, b, l) * ( f(t,k,m,l) * n0[k] + g(t,k,m,l) * w[k])
  return s

def activity_stable(t, l, b, w, n0, m):
  s = n0[m] + w[m] * t
  for k in range(1, m):
    s = s + r(k, m, b, l) * (f_stable(t,k,m,l) * n0[k] + g_stable(t,k,m,l) * w[k])
  return s

def r(k, m, b, l):
  if(k == m):
    return 1.0
  else:
    p = 1.0
    for i in range(k, m):
      p = p * (b[i+1] * l[i])
    return p

def f(t,k,m,l):
  s = 0.0
  for i in range(k, m+1):
    p = 1.0
    for j in range(k, m+1):
      if(i != j):
        p = p * (1 / (l[i] - l[j]))
    s = s + numpy.exp(-1 * l[i] * t) * p
  s = (-1)**(m-k) * s
  return s

def g(t,k,m,l):
  pa = 1.0
  for i in range(k,m+1):
    pa = pa * l[i]
  pa = 1.0 / pa

  s = 0.0
  for i in range(k, m+1):
    pb = 1.0
    for j in range(k, m+1):
      if(i != j):
        pb = pb * (1 / (l[i]-l[j]))
    s = s + (1/l[i]) * numpy.exp(-l[i]*t) * pb

  return pa + s * (-1)**(m-k+1) 


def f_stable(t,k,m_in,l):
  m = m_in - 1

  p = 1.0
  for i in range(k, m+1):
    p = p * l[i]

  s = 0.0
  for i in range(k, m+1):
    r = l[i]
    for j in range(k, m+1):
      if(i != j):
        r = r * (l[i] - l[j])
    s = s + (1/r)*numpy.exp(-1*l[i]*t)
  
  return (1.0/p) + s * (-1.0)**(m-k+1)


def g_stable(t,k,m_in,l):
  m = m_in - 1

  pa = 1.0
  for i in range(k,m+1):
    pa = pa * l[i]
  pa = t / pa

  sa = 0.0
  for i in range(k, m+1):
    pb = 1.0
    for j in range(k,m+1):
      if(j != i):
        pb = pb * l[j]
    sa = sa + pb
  pc = 1.0 
  for i in range(k, m+1):
    pc = pc * l[i]**2

  sb = 0.0
  for i in range(k, m+1):
    pd = 1.0
    for j in range(k, m+1):
      if(i != j):
        pd = pd * (1 / (l[i]-l[j]))
    sb = sb + (1/(l[i]**2)) * numpy.exp(-l[i]*t) * pd

  return 1.0/pa + sa / pc + sb * (-1)**(m-k+1)  





b = numpy.zeros((4,),)
b[2] = 1.0
b[3] = 1.0

w = numpy.zeros((4,),)
w[1] = 0.0
w[2] = 0
w[3] = 0

l = numpy.zeros((4,),)
l[1] = 1.09835073296562E-05
l[2] = 8.00456360209651E-09
l[3] = 0.0

n0 = numpy.zeros((4,),)
n0[1] = 10.0
n0[2] = 0.0
n0[3] = 0.0

t = 60000

activity(t, l, b, w, n0)

