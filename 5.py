import random

countries = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'Mexico', 'Russia', 'Spain', 'United Kingdom', 'United States']
country = random.choice(countries)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 5

print("Welcome to the Country Name Guessing Game!")
print("Can you guess the name of the country?")

# Display initial word
displayed = ''
for letter in country:
    if letter == ' ':
        displayed += ' '
    else:
        displayed += '-'
print(displayed)

while True:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in country.lower():
        print("Correct!")
    else:
        print("Incorrect!")
        wrong_guesses += 1
        if wrong_guesses >= max_wrong_guesses:
            print("Sorry, you've made too many wrong guesses. The country was", country)
            break

    # Display word with correctly guessed letters
    displayed = ''
    for letter in country:
        if letter.lower() in guessed_letters:
            displayed += letter
        elif letter == ' ':
            displayed += ' '
        else:
            displayed += '-'
    print(displayed)

    if '-' not in displayed:
        print("Congratulations! You've guessed the country correctly:", country)
        break
