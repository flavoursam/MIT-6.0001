# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist



def choose_word(wordlist):
	"""
	wordlist (list): list of words (strings)
	
	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing; assumes all letters are
	  lowercase
	letters_guessed: list (of letters), which letters have been guessed so far;
	  assumes that all letters are lowercase
	returns: boolean, True if all the letters of secret_word are in letters_guessed;
	  False otherwise
	'''
	for char in secret_word:
		if char not in letters_guessed:
			return False
		else:
			return True


def get_guessed_word(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string, comprised of letters, underscores (_), and spaces that represents
	  which letters in secret_word have been guessed so far.
	'''
	partial = ""
	for char in secret_word:
		if char not in letters_guessed:
			partial += "_ "
		else:
			partial += char
	return partial


def get_available_letters(letters_guessed):
	'''
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string (of letters), comprised of letters that represents which letters have not
	  yet been guessed.
	'''
	remaining_letters = ""
	for char in string.ascii_lowercase:
		if char not in letters_guessed:
			remaining_letters += char
	return remaining_letters
	

def hangman(secret_word):
	'''
	secret_word: string, the secret word to guess.
	
	Starts up an interactive game of Hangman.
	
	* At the start of the game, let the user know how many 
	  letters the secret_word contains and how many guesses s/he starts with.
	  
	* The user should start with 6 guesses

	* Before each round, you should display to the user how many guesses
	  s/he has left and the letters that the user has not yet guessed.
	
	* Ask the user to supply one guess per round. Remember to make
	  sure that the user puts in a letter!
	
	* The user should receive feedback immediately after each guess 
	  about whether their guess appears in the computer's word.

	* After each guess, you should display to the user the 
	  partially guessed word so far.
	
	Follows the other limitations detailed in the problem write-up.
	'''
	print("Welcome to the game Hangman!")
	print("I am thinking of a word that is", len(secret_word), "letters long.")
	guesses_remaining = 6
	warnings_remaining = 3
	letters_guessed = []
	print("You have", warnings_remaining, "warnings left.")
	while guesses_remaining > 0:
		partial = get_guessed_word(secret_word, letters_guessed)
		print("-------------")
		
		if partial == secret_word:
			totalScore(guesses_remaining, secret_word)
			break

		print("You have", guesses_remaining, "guesses left.")
		print("Available letters:", get_available_letters(letters_guessed))
		guess = input("Please guess a letter: ")
		guess = guess.lower()

		if guess.isalpha() and guess in secret_word and guess not in letters_guessed:
			letters_guessed.append(guess)
			print("Good guess:", get_guessed_word(secret_word, letters_guessed))

		elif not guess.isalpha() or len(guess) > 1 or guess in letters_guessed:
			if warnings_remaining > 0:
				warnings_remaining -= 1
				print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:")
				print(partial)
			else:
				print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", partial)
				guesses_remaining -= 1

		elif guess not in secret_word:
			vowels = "aeiou"
			if guess in vowels:
				guesses_remaining -= 2
			else:
				guesses_remaining -= 1
			letters_guessed.append(guess.lower())
			print("Oops! That letter is not in my word:", partial)

	if guesses_remaining == 0:
		return lose(secret_word)


def lose(secret_word):
	print("-------------")
	print("Sorry, you ran out of guesses. The word was", secret_word)


def totalScore(guesses_remaining, secret_word):
	num_of_distinct_letters = len(list(set(secret_word)))
	score = guesses_remaining * num_of_distinct_letters
	print("Congratulations, you won!")
	print("Your total score for this game is:", score)
	return score


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
	'''
	my_word: string with _ characters, current guess of secret word
	other_word: string, regular English word
	returns: boolean, True if all the actual letters of my_word match the 
		corresponding letters of other_word, or the letter is the special symbol
		_ , and my_word and other_word are of the same length;
		False otherwise: 
	'''
	my_word_stripped = my_word.replace(" ", "")
	for x, y in zip(my_word_stripped, other_word):
		if (x != "_" and x != y) or (x == "_" and y in my_word) or (len(my_word_stripped) != len(other_word)):
			return False
	return True


def show_possible_matches(my_word):
	'''
	my_word: string with _ characters, current guess of secret word
	returns: nothing, but should print out every word in wordlist that matches my_word
			 Keep in mind that in hangman when a letter is guessed, all the positions
			 at which that letter occurs in the secret word are revealed.
			 Therefore, the hidden letter(_ ) cannot be one of the letters in the word
			 that has already been revealed.
	'''
	my_word_stripped = my_word.replace(" ", "")
	result = []
	for word in wordlist:
		if match_with_gaps(my_word_stripped, word):
			result.append(word)
			print(word)
	if not result:
		print("No matches found.")

			

def hangman_with_hints(secret_word):
	'''
	secret_word: string, the secret word to guess.
	
	Starts up an interactive game of Hangman.
	
	* At the start of the game, let the user know how many 
	  letters the secret_word contains and how many guesses s/he starts with.
	  
	* The user should start with 6 guesses
	
	* Before each round, you should display to the user how many guesses
	  s/he has left and the letters that the user has not yet guessed.
	
	* Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
	  
	* The user should receive feedback immediately after each guess 
	  about whether their guess appears in the computer's word.

	* After each guess, you should display to the user the 
	  partially guessed word so far.
	  
	* If the guess is the symbol *, print out all words in wordlist that
	  matches the current guessed word. 
	
	Follows the other limitations detailed in the problem write-up.
	'''
	print("Welcome to the game Hangman!")
	print("I am thinking of a word that is", len(secret_word), "letters long.")
	guesses_remaining = 6
	warnings_remaining = 3
	letters_guessed = []
	print("You have", warnings_remaining, "warnings left.")
	print("Input '*' to get a list of possible word matches.")

	while guesses_remaining > 0:
		# instance of secret word ie. the current guess of the word
		partial = get_guessed_word(secret_word, letters_guessed)
		print("-------------")
		
		# if win
		if partial == secret_word:
			totalScore(guesses_remaining, secret_word)
			break

		# game information and instructions
		print("You have", guesses_remaining, "guesses left.")
		print("Available letters:", get_available_letters(letters_guessed))
		guess = input("Please guess a letter: ")
		guess = guess.lower()
		
		# if guess is alphanumeric, in the secret word and has not been guessed yet
		# store letter, print instance of guessed word
		if guess.isalpha() and guess in secret_word and guess not in letters_guessed:
			letters_guessed.append(guess)
			print("Good guess:", get_guessed_word(secret_word, letters_guessed))

		# if hint is requested
		elif guess == "*":
			print("Possible word matches are:")
			print(show_possible_matches(partial))

		# if guess is not alphanumeric, longer than 1 char or has been guessed already
		# deduct warnings or gusseses accordingly
		elif not guess.isalpha() or len(guess) > 1 or guess in letters_guessed:
			if warnings_remaining > 0:
				warnings_remaining -= 1
				print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:")
				print(partial)
			else:
				print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", partial)
				guesses_remaining -= 1
		
		# if guess not in secret word
		# deduct guesses accordingly
		# store letter
		elif guess not in secret_word:
			vowels = "aeiou"
			if guess in vowels:
				guesses_remaining -= 2
			else:
				guesses_remaining -= 1
			letters_guessed.append(guess.lower())
			print("Oops! That letter is not in my word:", partial)

	# if lose
	if guesses_remaining == 0:
		return lose(secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
	# secret_word = choose_word(wordlist)
	# hangman("tact")

	secret_word = choose_word(wordlist)
	hangman_with_hints(secret_word)
