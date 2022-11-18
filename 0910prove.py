print()
print("Welcome!")
print()

items = []
prices = []
add_item = None
action = None
price = 0
total = 0
number_items = 0

while action != "5":
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("Please enter an action: ")
    if action != "5":
        if action == "1":
            add_item = input("What item would you like to add? ")
            price = float(input(f"What is the price of '{add_item}'? "))
            items.append(add_item)
            prices.append(price)
            print(f"'{add_item}' has been added to the cart.")
            number_items = number_items + 1
            print()

        elif action == "2":
            print(f"The contents in your cart are ({number_items}):")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i - 1]} - ${prices[i - 1]:.2f}")
            print()
        
        elif action == "3":
            remove_item = int(input("Which item would you like to remove? "))
            items.pop(remove_item)
            prices.pop(remove_item)
            print("Item removed.")
            print()
        
        elif action == "4":
            total = sum(prices)
            print(f"The total price of the items in the shopping cart is ${total:.2f}")
            print()
    
print("Have a nice day.")
print()

























# print()

# items = []
# item = ""
# while item != "end":

#     item = input("What item would you like to add from the list? ")

#     if item != "end":
#         items.append(item)

# print()
  

# for item in items:
#     print(item)