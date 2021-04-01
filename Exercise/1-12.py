import math

t1 = float(input("Enter the value x of a point on Earth in degrees: "))
t2 = float(input("Enter the value y for that point on Earth in degrees: "))

g1 = float(input("Enter the value x of a second point on Earth in degrees: "))
g2 = float(input("Enter the value y for that point on Earth in degrees: "))

distance = 6371.01 * math.acos(math.sin(math.radians(t1)) * math.sin(math.radians(g1)) + math.cos(math.radians(t1)) * math.cos(math.radians(g1)) * math.cos(math.radians(t2 - g2)))

print("The distance between the two points on Earth is {}km" .format(distance))
