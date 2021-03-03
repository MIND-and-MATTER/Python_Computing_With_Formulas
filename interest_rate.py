# Compute growth of bank account from intrest

A = float(input("Input initial ammount invested:")) 
n = float(input("Input time of investment (years):"))    
p = float(input("Input intrest rate (%):")) 

f = (1 + (p / 100))**n                # Compute proportionality 
Af = A * f

print ("After %g yearse an initial investment of %g at %g percent intrest will have a value of %.2f" % (n, A, p, Af)) 