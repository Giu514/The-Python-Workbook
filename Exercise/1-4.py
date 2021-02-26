#write area of field in acres

width =float(input("insert the width of field in feet: "))
lenght = float(input("insert the lenght of field in feet: "))
acres = width * lenght/43560
print("The area of the field in acres is: {:.3f}".format(acres))
