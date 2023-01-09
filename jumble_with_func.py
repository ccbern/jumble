import requests
import random

### GET LIST OF WORDS ###
def get_word_list(word_site):
	word_list = []
	response = requests.get(word_site)
	words = response.content.splitlines()

	for w in words:
		word_list.append(w.decode('ASCII'))

	return word_list

### PARE WORD LIST BY LENGTH ###
def pare_words_by_length(min_length,max_length):
	pared_word_list = []

	for word in word_list:
		if len(word) >= min_length and len(word) <= max_length:
			pared_word_list.append(word)

	return pared_word_list

### PICK NEW WORD ###
def pick_new_word(pared_word_list):
	random_word_num = random.randrange(len(pared_word_list))
	random_word = pared_word_list[random_word_num]

	### REMOVE PICKED WORD FROM WORD LIST ###
	pared_word_list.remove(random_word)

	return random_word

### JUMBLE AND PRINT WORD ###
def jumble_word(word):
	random_order = []  ### CLEARED TWICE -- BOO ###
	random_order_string = ''
	word_to_break = word

	### vv Why adding to existing string? vv ###
	for letter in word_to_break:
		random_let_num = random.randrange(len(word_to_break))
		random_letter = word_to_break[random_let_num]
		word_to_break = word_to_break.replace(random_letter,'',1)
		random_order.append(random_letter)

	random_order_string = ''.join(random_order)

	return random_order_string
	### ^^ Why adding to existing string? ^^ ###

### GUESSING ###
def try_guess(guess,random_word):
	correct_guess = False
	if guess.lower() == random_word.lower():
		correct_guess = True
		return True

	else:
		return False

### RUN GAME ###
print("Let's play JUMBLE!")

word_list = get_word_list("https://www.mit.edu/~ecprice/wordlist.10000")

### GET LENGTH FROM USER ###
min_length = int(input('Minimum word length: '))
max_length = int(input('Maximum word length: '))

pared_word_list = pare_words_by_length(min_length,max_length)

correct_guesses = 0
current_streak = 0
highest_streak = 0
new_word = True

while new_word:
	guess_count = 0
	random_word = pick_new_word(pared_word_list)
	jumbled_word = jumble_word(random_word)
	print('')
	print(jumbled_word)
	print('')

	correct = False

	while not correct:
		print('Guess the word!')  
		print('Type "Scramble" to re-jumble the letters or "Give up" for the answer.')
		guess = input('Guess: ')

		if guess.capitalize() == 'Give up':
			print('Too bad!  The word was %s' % random_word.upper())
			correct = True

			if current_streak != 0:
				print('Streak lost!  Previous streak was: %i' % current_streak)
			
			current_streak = 0

		elif guess.capitalize() == 'Scramble':
			rescrambled_word = jumble_word(jumbled_word)
			print(rescrambled_word)
			
		else:
			guess_count += 1

			if try_guess(guess,random_word):
				print('You got it!  The word was %s' % random_word.upper())
				correct_guesses += 1
				correct = True

				if guess_count == 1:
					current_streak += 1

					if current_streak > highest_streak:
						highest_streak = current_streak
						print('New high streak!')

				print('Current streak is: %i' % current_streak)

			else:
				if current_streak != 0:
					print('Streak lost!  Previous streak was: %i' % current_streak)
				print('Try again!')
				current_streak = 0

	replay = input('Another word?  "Y" or "N": ').upper()
	
	while replay not in ['Y','N']:
		replay = (input('Please choose "Y" or "N": ').upper())

	if replay == 'N':
		print('You got %i words correct this time.' % correct_guesses)
		print('Your highest streak was: %i' % highest_streak)
		print('Thanks for playing!')
		new_word = False
