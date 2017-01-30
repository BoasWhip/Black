import math
import numpy as np

a = np.array([[2,3,4], [1,2,3]])
b = a * 1.0
c = a[1][1] * 1.0
print c
cvalue = [25.4, 24.8, 26.9, 23.9]
C = np.array(cvalue)
print (C*9/5 + 32)[0]
print np.array([1,4,9,15])//5.0
print np.arange(0, 10, 0.5, dtype = None)

L, S = np.linspace(0, 50, num = math.pi, retstep=True)
print S
x = np.array([[42,1,2],[1,2,3]])
print x[1][1]
print x%3
print x.ndim
y = np.array([0., 1, 2, 3, 4., 5., 8, 13])
print y / 1.0
print y[1:4]*math.pi
print x[0, 1:]

define = (3,3)
x = np.array([range(0, 51, 5),[x for x in range(0,255,25)],[True,True,True,True,True,False,False,False,False,False]]) 
s = x[0][:6]
s[1] *= 8.5
print x[0][:6]
print s == x[0][:6]

t = np.zeros((9))
print t

t = t.reshape(3,3)
print t

x = np.ones((3,3))
y = np.ones_like(x)
z = np.identity(5, dtype=float)
q = (np.eye(3,k=-1, dtype=int) + np.eye(3,k=+1, dtype=int)) * 4
print q
print z
print np.random.random(define)
print np.empty(define)
print np.average(z)
print np.median(z) < np.average(z)
print np.std(z[0])
print np.max(z) * math.e
g = np.dot(q, z[:3,:3]) / 2.5
print g
