# Compute the mass of 1 liter of each of the following substances whos densities are given in g/cm^3 

## 1 cm^3 = 1 ml   ( 
### 1 l = 1000 ml
###  (g/cm^3)(10^3) = g/l

Fe = float(7.87)                 # Density of iron
air = float(0.001207)            # Density of air
fule = float(0.83)               # Density of gassoline
ice = float(0.916)               # Density of ice
Hu = float(1.01)                 # Density of human body
Ag = float(10.49)                # Density of silver
Pt = float(21.45)                # Density of platinum

#### Compute & print mass/liter of the substances

print("The mass of 1 liter of iron  is %g grams" %  (Fe*10**3))
print("The mass of 1 liter of air is %g grams" %  (air*10**3))
print("The mass of 1 liter of gassoline is %g grams" %  (fule*10**3))
print("The mass of 1 liter of ice is %g grams" %  (ice*10**3))
print("The mass of 1 liter of the huma body is %g grams" %  (Hu*10**3))
print("The mass of 1 liter of silver is %g grams" % (Ag*10**3))
print("The mass of 1 liter of platinum is %g grams" %  (Pt*10**3))      
