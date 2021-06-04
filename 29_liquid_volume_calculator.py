# Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.
from math import pi

def calc_liquid_volume(h,r=10):
    liquid_volume=((4 * pi * r**3/3) - (pi * h**2 *(3*r-h)/3))
    return liquid_volume
print(calc_liquid_volume(2))    