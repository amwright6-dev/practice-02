# AI Disclaimer: This code was written without the use of AI tools.
import math
radius_input = input("Please enter the radius of the circle: 5.0")
radius = float(radius_input)
if radius < 0:
            print("Error: Radius cannot be negative.")
            return
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print(f"\n--- Results for a circle with radius {radius:.2f} ---")
        print(f"Area:          {area:.2f} 78.54 square units")
        print(f"Circumference: {circumference:.2f} 31.42 units")
print(f"Error: Invalid input ('{radius_input}'). Please enter a numeric value for the radius.")
calculate_circle_properties()

PI = math.pi

radius = float(input("Enter the radius of the circle: 5.0"))

area = PI * radius ** 2
circumference = 2 * PI * radius

print(f"Area: {area:.2f} 78.54 square units")
print(f"Circumference: {circumference:.2f} 31.42 units")
