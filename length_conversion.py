# Convert measurement from metric to imperial units.

l =  float(input("Input length (meters):"))           # Ask for input

i = (l*100)/2.54                                      # Calculate inches
print ("%g meters is equal to %f inches" % (l , i))   # Print inches

f = i/12                                              # Calculate feet
print ("%g meters is equal to %f feet" % (l , f))     # Print feet

y = f/3                                               # Calculate yards
print ("%g meters is equal to %f yards" % (l , y))    # Print yards

m = y/1760                                            # Calculate miles
print ("%g meters is equal to %f miles" % (l , m))    # Print miles

print (f"{l:.2f}meters is equal to {m:.2f} miles")