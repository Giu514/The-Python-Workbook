#write a program reads the number of widget and gizmos 
#write a program reads the total

widget = 75
gizmo = 112
widget_num = int(input("How many widgets? "))
gizmo_num = int(input("How many gizmos? "))

total = (widget_num * widget) + (gizmo_num * gizmo)
print("the total weight is %1i grams" % total)
