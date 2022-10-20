from cmath import pi


print()
square = input("What is the length of a side of the square? ")
square_len = float(square)
square_area = square_len**2
print("The are of the square is: "+ str(square_area) +"")
print()
rectangle_len = float(input("What is the length of the rectangle? "))
rectangle_wid = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_len*rectangle_wid
print(f"The area of the rectangle is: {rectangle_area}")
print()
circle_rad = float(input("What is the radius of the circle? "))
circle_area = pi*circle_rad**2
print(f"The area of the circle is: {circle_area}")
print()