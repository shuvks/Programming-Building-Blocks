friends = []

friend_name = ""
while friend_name != "end":
    friend_name = input("Type the name of a friend: ")

    if friend_name != "end":
        friends.append(friend_name)

print()
print("Your friends are:")
for friend_name in friends:
    print(f"{friend_name}")