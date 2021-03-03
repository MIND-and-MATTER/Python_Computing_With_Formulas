# How to cook the perfect egg.

from math import log, pi

M = float(input("Input mass of the egg (g):"))

To =  float(input("Input initial temperature of the egg (degree C):"))    
Tw =  float(input("Input initial temperature of the water (degree C):"))  
Ty =  float(input("Input desired temperature of the yolk (degree C):"))

p = 1.038                     # density of an egg (g/cm^3)
c = 3.7                       # Specific heat capacity of an egg
K = 5.4E-3                    # Thermal conductivity constant

               

##  Implement the formula in a program, set Tw = 100 C and Ty = 70 C, and compute t for a large egg taken from the fridge (To = 4 C) and from room temperature (To = 20 C).

N = (M**(2/3) * c * p**(1/3))
D = (K * pi**2) * ((4 * pi) / 3)**(2/3)  

C = N / D                                     # Compute conatant factor

V = log((0.76 * (To - Tw)) / (Ty - Tw))       # Compute variable factor

t = (C * V) / 60                              # Compute time in minutes

print(f" The it will take {t:.2f} minutes to cook your prefect egg.")