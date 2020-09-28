"""
circle1.py
circumference, area and radius calculation
created by sands 30/10/10
"""

from math import pi, sqrt

def circ(diam):
    """
    calculates circumference of circle
    argument: diam (diameter) : float
    returns: circumference : float
    """
    return(pi * diam)

def area(diam):
    """
    calculates area of circle
    argument: diam (diameter) : float
    returns: area : float
    """
    radius = diam / 2
    return(pi * radius * radius)

def rad(area) :
      """
      calculates radius of a circle given the area
      argument: area : float
      returns: radius : float
      """
      return sqrt(area/pi)


print(format("Diam",">4s") + format("Circum",">8s") + format("Area",">8s"))
diam = 0.5
while diam <= 10.0 :
    print(format(diam,"4.1f") + format(circ(diam),"8.3f") + format(area(diam),"8.3f"))
    diam = diam + .5

area = float(input("\nenter area of a circle (real number > 0) : "))
print("radius of the circle is :", format(rad(area),"8.3f"))