#This is also assignment 04prove.py
print()
print("Attention: For Employee Viewing and Use Only.")
print()
child_meal = float(input("Enter the price of a child's meal: "))
adult_meal = float(input("Enter the price of an adult's meal: "))
sliced_fruit_price = float(input("Enter the price of the sliced fruit: "))
cookie_price = float(input("Enter the price of the cookie: "))
chips_price = float(input("Enter the price of the chips: "))
print()
num_child = int(input("Enter the number of children: "))
num_adult = int(input("Enter the number of adults: "))
sliced_fruit = int(input("Enter the number of sliced fruit orders: "))
cookie = int(input("Enter the number of cookie orders: "))
chips = int(input("Enter the number of chip orders: "))
print()
tax = float(input("Enter the sales tax rate: "))
child_total = child_meal*num_child
adult_total = adult_meal*num_adult
slice_fruit_total = sliced_fruit_price*sliced_fruit
cookie_total = cookie_price*cookie
chips_total = chips_price*chips
sides = slice_fruit_total+cookie_total+chips_total
subtotal = child_total+adult_total+sides
sales_tax = subtotal*tax / 100
total = subtotal+sales_tax 
discount = float(input("Enter discount amount (if none, enter 0): "))
total_with_discount = total - discount
print()
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Total: ${total_with_discount:.2f}")
print()
payment = float(input("What is the payment amount? "))
change = payment-total_with_discount
print(f"Change: ${change:.2f}")
print()
print("Thank you for eating at Chubby's. Come again soon!")
print()