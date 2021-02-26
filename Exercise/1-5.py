#write program reads the numeber of containers of each size and the refund

less_1l_containers = 0.10
more_1l_containers = 0.25

less = int(input("How many containers one litre or less have? "))
more = int(input("How many containers more than one litre have? "))

refund = less * less_1l_containers + more * more_1l_containers

print("You will be compensated for: ${:.2f}".format(refund))
