from hangman_stages import hangmen

word_list = open("word_list.txt", "r")
alternative_target_words = word_list.read().splitlines()  # All words that the the player hasn't ruled out
word_list.close()
guesses = []
won = False  # Whether the game has been won

def game_state(word, found_letters, hangman_stage):
    """
    Displays what letter have been found, and how many incorrect letters have been guessed.
    :param word: The word to find.
    :param found_letters: The letters the have been found.
    :param hangman_stage: The the stage in the hangman's hanging.
    :return: A display of the game's state.
    """
    word_line = ""

    for character in word:
        word_line += (character if character in found_letters else "_") + " "

    previously_guessed = ""

    for past_guess in sorted(guesses):
        previously_guessed += past_guess + " "

    return word_line + "\tGuessed: " + previously_guessed[:-1] + hangmen[hangman_stage]


word_length = int(input("How many letters do you want in the word?: "))
print("Ok, let's begin.")

# Restrict possible words to words of the right size
alternative_target_words = [word for word in alternative_target_words if len(word) == word_length]
target_word = alternative_target_words[0]

# Guessing loop
incorrect_guesses = 0

while incorrect_guesses < 11:
    print(game_state(target_word, guesses, incorrect_guesses))

    # Check if the player has won
    won = True

    for letter in target_word:
        if letter not in guesses:
            won = False
            break

    if won:
        print("You win! The word is \"" + target_word + "\" 😊")
        break

    # Get next guess from player
    guess = input("Next letter: ")[0].lower()

    if guess not in guesses:
        guesses += [guess]

    # Remove words that could cause a win
    alternative_target_words = [word for word in alternative_target_words if guess not in word]

    # Find a word that could cause a win
    target_word = alternative_target_words[0] if len(alternative_target_words) > 0 else target_word

    # Allow the guess to succeed only if we can't change the target word
    if len(alternative_target_words) == 0 and guess in target_word:
        print("✅ In the word.")
    else:
        print("❌ Not in the word.")
        incorrect_guesses += 1

if not won:
    print("You lose, the word is \"" + target_word + "\" ☹️" + hangmen[-1])
