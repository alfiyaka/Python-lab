from Graphics.rectangle import *
from Graphics.circle import *
from Graphics.Dgraphics.sphere import *
from Graphics.Dgraphics.cuboid import *
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle perimeter=",RectPerimeter(l,b))

r=int(input("Enter radius of circle:"))
print("Circle Area=",CirArea(r))
print("Circle Perimeter=",CirPerimeter(r))

r=int(input("Enter radius of sphere:"))
print("Sphere Area=",SpArea(r))
print("Sphere volume=",SpPerimeter(r))

l=int(input("Enter cuboid length:"))
b=int(input("Enter cuboid breadth:"))
h=int(input("Enter cuboid height:"))
print("Cuboid Area=",CubArea(l,b,h))
print("Cuboid Perimeter=",CubPerimeter(l,b,h))











