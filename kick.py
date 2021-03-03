# Calculate the air resistance on a football

import math

V1 = 120 / 3.6
V2 = 10 / 3.6
C = (1.2 * 0.2) / 2

Fg = 9.81 * 0.43
A = math.pi * 0.11

Fd1 = C * A * V1**2
Fd2 = C * A * V2**2

Ratio1 = Fd1 / Fg
Ratio2 = Fd2 / Fg

print(f"The fore of air resistance on a football kicked at 120 km/h is {Fd1:.2f}N. This ammounts to {Ratio1:.2f} percent of the force of gravity acting on the ball.")

print(f"The fore of air resistance on a football kicked at 10 km/h is {Fd2:.2f}N. This ammounts to {Ratio2:.2f} percent of the force of gravity acting on the ball.")
