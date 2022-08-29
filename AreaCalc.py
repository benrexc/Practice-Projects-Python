# Create a simple calculator to calculate the area of a circle and a triangle #
# Program will prompt user to select a shape, calculate the area of a shape, print the area of the shape to the user #

print("Calculator initializing \n ... \n ...")


option = raw_input("Enter C for Circle or T for Triangle: \n")
if option == "C":
  radius = float(raw_input("Enter radius: "))
  area = 3.1419 * radius **2
  print("Area: %f" % area)
elif option == "T":
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = (base * height)/2
  print("Area: %f" % area)
else: print("not a valid entry")
print("... \n...")
print("calculator is now terminating")








