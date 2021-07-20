# hangmanCheater
A game of Hangman where the person with the target word cheats to prevent you from winning.

As you play, the program tries as hard as it can to not give you any letters in the word. It does this my reducing the set of all words it could be to only those words of the right length, that you have not guessed. If you have guessed letters which prevent the program from cheating (there are not alternative words it could be), it pretends that it was never cheating and plays a proper game of Hangman from that point onwards.
