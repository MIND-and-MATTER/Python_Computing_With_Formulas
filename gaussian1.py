
from numpy import exp
from math import pi, sqrt

# Evaluatethe Gaussian Function

m = float(input("Input value for m: "))
s = float(input("Input value for s: "))
x = float(input("Input value for x: "))

e = exp((-1/2) * ((x - m) / s)**2)
y = e / (sqrt(2*pi)*s)

print (y)
