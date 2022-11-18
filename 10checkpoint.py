the_list = []
item = None

print("Please enter the items of the shopping list (type: quit to finish):")

while item != "quit":
    item = input("Item: ")

    if item!= "quit":
        the_list.append(item)

print("The shopping list is:")
for item in the_list:
    print(item)

print("The shopping list with indexes is:")
for i in range(len(the_list)):
    item = the_list[i]
    print(f"{i}. {item}")

print()
index = int(input("Which item would you like to change?"))
new_item = input("What is the new item? ")

the_list[index] = new_item

print("The shoping list with indexes is:")
for i in range(len(the_list)):
    item = the_list[i]
    print(f"{i}. {item}")