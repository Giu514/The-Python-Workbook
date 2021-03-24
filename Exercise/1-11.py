#Fuel Efficiency covert from mpg to L/100 KM



miles = float(input("Enter the number of miles done: "))
gallons = float(input("Enter the number of gallons consumed: "))
mpg = float(miles/gallons)
can = float(235.214583 / mpg)

print("{} mpg, equivalent to {:.2f} L/100km".format(mpg, can))
