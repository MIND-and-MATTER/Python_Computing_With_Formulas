# Can a baby in Norway expect to live for 1 billion seconds? 

s = 10**9
m = s / 60              # number of minutes     
h = m /60               # number of hours 
d = h / 24              # number of days
y = d / 365             # number of years
leep = y / 4            # calculate error from leep years      
D = d - leep            # adjust for leap years 
Y = D / 365             # number of years adjusted for leap years
print ("One billion seconds is equal to %g years" % (Y))