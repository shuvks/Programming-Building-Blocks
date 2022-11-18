SecretWord = "art"
guess = ""
num_guesses = 0

print("Your hint is: ", end= "")
for letter in SecretWord:
    print("_ ", end="")
print()
while guess != SecretWord:
    guess = input("What is your guess? ")
    hint = ""
    num_guesses = num_guesses +1
    for i, letter in enumerate(SecretWord):
        if i < len(guess) and letter.lower() == (guess)[i]:
            hint += letter.upper()
        elif letter.lower() in guess:
            hint += letter.lower()
        else:
            hint += "_ "
    print(f"Your hint is: {hint}")
print("Congratulations! You guessed it.")
print(f"It took you {num_guesses} guesses.")
