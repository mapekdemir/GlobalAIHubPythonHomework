"""
Take 5 values the user and write a program that prints the values you get on the screen.
Print the of values you received in this program the screen.
When using print functions, do not forget to f-string and format usage in program
"""
val1 = input("Enter the string value: ")
val2 = int(input("Enter the integer value: "))
val3 = float(input("Enter the float value: "))
val4 = bool(input("Enter the bool value: "))
val5 = list(input("Enter the list value: "))

tval1 = type(val1)
tval2 = type(val2)
tval3 = type(val3)
tval4 = type(val4)
tval5 = type(val5)

print(f"""
First Value  : {val1} -- Type: {str(tval1)[8:-2]}
Second Value : {val2} -- Type: {str(tval2)[8:-2]}
Third Value  : {val3} -- Type: {str(tval3)[8:-2]}
Fourth Value : {val4} -- Type: {str(tval4)[8:-2]}
Fifth Value  : {list} -- Type: {str(tval5)[8:-2]}
""")