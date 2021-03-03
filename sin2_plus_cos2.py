
from math import sin, cos, pi

# Does sin^2(x) + cos^2(x) = 1 ?

x = pi/4
val = sin(x)**2 + cos(x)**2

print (val)

## Compute s in meters when s = v0t + 0.5at^2, with v0 = 3 m/s, t = 1 s,                a = 2 m/s^2.

v0 = 3                             # Meters per second
t = 1                              # Seconds
a = 2                              # Meters * seconds^-2
s = (v0 * t) + (0.5 * a * (t**2))
print (s)

### Verify these equations:
#### Eq 1: (a + b)^2  = a^2 + 2ab + b^2
##### Eq 2: (a  b)^2 = a^2 - 2ab + b^2

a = 3 
b = 5
a2 = a**2
b2 = b**2

eq1sum = a**2 + 2*a*b + b**2
eq1pow = (a + b)**2
print("%.3f is equal to %.3f" % (eq1sum, eq1pow))

eq2sum = a**2 - 2*a*b + b**2
eq2pow = (a - b)**2
print("%.3f is equal to %.3f" % (eq2sum, eq2pow))