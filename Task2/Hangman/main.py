import random

# List of words for game play
words_with_hints = [
    ('python', 'A programming language'),
    ('hangman', 'A classic word guessing game'),
    ('challenge', 'Something difficult to overcome'),
    ('programming', 'What you are doing right now'),
    ('microsoft', 'A tech giant known for Windows'),
    ('computer', 'An electronic device for computation'),
    ('science', 'A systematic enterprise that builds knowledge'),
('google', 'Search engine giant'),

    ('facebook', 'Social media platform now known as Meta'),
    ('instagram', 'Social media platform now known as Meta'),
    ('apple', 'A fruit and a tech company'),
]

def get_hint(word, guessed_letters):
    hint = ''
    for letter in word:
        if letter in guessed_letters:
            hint += letter
        else:
            hint += '_ '
    return hint

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def play_hangman():
    word, hint = random.choice(words_with_hints)
    guessed_letters = []
    tries = 6
    print("Welcome to Hangman!")

    while tries > 0:
        print(display_hangman(tries))
        print(f"Hint: {hint}")
        guess = input(f"Word: {get_hint(word, guessed_letters)}\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            tries -= 1
            print("Incorrect guess.")

        if set(word) <= set(guessed_letters):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(display_hangman(tries))
        print(f"Game over! The word is: {word}")

play_hangman()
