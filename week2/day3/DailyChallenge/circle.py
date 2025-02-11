import math
from turtle import *

class Circle:
    def __init__(self, d_or_r, value):
        if d_or_r == "d":
            self.diameter = value
            self.radius = self.diameter / 2
        else:
            self.radius = value
            self.diameter = self.radius * 2

    def area(self):
        return math.pi * (self.radius**2)
    
    def __str__(self):
        return f"Diameter : {self.diameter}, Radius : {self.radius}"

    def __add__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            return Circle("r", new_radius)
        else:
            raise TypeError("Only circles can be added together.")
    
    def __lt__(self, other): # self < other
        return self.radius < other.radius
    
    def __gt__(self, other): # self > other
        return self.radius > other.radius
    
    def __eq__(self, other): # self == other
        return self.radius == other.radius


    @staticmethod
    def get_circle():
        d_or_r = input("Would you like to enter the diameter or the radius ? (d or r) : ")

        value = 0.0
        while d_or_r != "d" and d_or_r != "r": 
            print("You entered a wrong answer. Please enter 'd' for diameter or 'r' for radius.")   
            d_or_r = input("Would you like to enter the diameter or the radius ? (d or r) : ")
            
        if d_or_r == "d":
            value = float(input("Enter the diameter value : "))
        elif d_or_r == "r":
            value = float(input("Enter the radius value : "))
        
        return Circle(d_or_r, value)

circles = []

circle1 = Circle.get_circle()
circles.append(circle1)
print(f"Area of the first circle : {circle1.area():.2f}")  
print(circle1)

print("\n================================")
circle2 = Circle.get_circle()
circles.append(circle2)
print(f"Area of the second circle : {circle2.area():.2f}")  
print(circle2)

print("\n================================")
print("New circle :")
circle3 = circle1 + circle2
circles.append(circle3)
print(f"Area of the new circle : {circle3.area():.2f}")  
print(circle3)

print("\n================================")
print(f"circle1 < circle2 ? {circle1 < circle2}")
print(f"circle1 > circle2 ? {circle1 > circle2}")
print(f"circle1 == circle2 ? {circle1 == circle2}")

print("\n================================")
print("=== Sorted circles ===")
circles.sort()
for circle in circles:
    print(circle)

print("\n================================")
# ========== Turtle ==========
def turtle_circles(circles):
    turtle = Turtle()
    turtle.penup()

    start_x = -200
    for c in circles:
        turtle.goto(start_x, -circle.radius)
        turtle.pendown()
        turtle.circle(c.radius)
        turtle.penup()

        start_x += circle.diameter
    
    turtle.hideturtle()
    turtle.done()

turtle_circles(circles)

