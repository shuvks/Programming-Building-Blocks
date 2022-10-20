from re import A


print()
grade = int(input("What is your grade percentage? "))
print()
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter ="B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade < 60:
    letter = "F"
print(f"Your grade is a(n) '{letter}'.")
if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")
