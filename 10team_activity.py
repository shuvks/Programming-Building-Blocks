names = []
balances = []
name = None
balance = None

print("Enter the name and balance of the bank account (type 'quit' for both when done).")
while name != "quit":
    name = input("Name: ")

    if name != "quit":
        balance = float(input("Balance: "))

        names.append(name)
        balances.append(balance)

total= 0
for i in range(len(names)):
    print(f"{names[i]} - ${balances[i]}")

    total += balances[i]

average = total /len(balances)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")