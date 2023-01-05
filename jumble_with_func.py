import requests
import random

word_list = []
pared_word_list = []
new_word = True
random_word = ''
random_order = ''

### GET LIST OF WORDS ###
def get_word_list(word_site):
	response = requests.get(word_site)
	words = response.content.splitlines()

	# word_list = []

	for w in words:
		word_list.append(w.decode('ASCII'))

### PARE WORD LIST BY LENGTH ###
def pare_words_by_length(min_length,max_length):
	# pared_word_list = []

	for word in word_list:
		if len(word) >= min_length and len(word) <= max_length:
			pared_word_list.append(word)

### PICK NEW WORD ###
def pick_new_word():
	# while new_word:
	guess = 'first'
	random_order = []
	random_word_num = random.randrange(len(pared_word_list))
	random_word = pared_word_list[random_word_num]

	### REMOVE PICKED WORD FROM WORD LIST ###
	pared_word_list.remove(random_word)

### JUMBLE AND PRINT WORD ###
def jumble_word(word):
	word_to_break = word
	
	for letter in word_to_break:
		random_let_num = random.randrange(len(word_to_break))
		random_letter = word_to_break[random_let_num]
		word_to_break = word_to_break.replace(random_letter,'',1)
		random_order.append(random_letter)

	random_order_string = ''.join(random_order)

	print(random_order_string)

### GUESSING ###
def try_guess(guess):
	correct_guess = False
	if guess == random_word:
		correct_guess = True
		return True

	else:
		return False

print("Let's play JUMBLE!")

get_word_list("https://www.mit.edu/~ecprice/wordlist.10000")

### GET LENGTH FROM USER ###
min_length = int(input('Minimum word length: '))
max_length = int(input('Max word length: '))

pare_words_by_length(min_length,max_length)

### RUN GAME ###
while new_word:
	pick_new_word()
	jumble_word(random_word)
	correct = False

	while not correct:
		guess = input('Guess the word!  For answer, type "Give up": ')

		if guess.capitalize() == 'Give up':
			print('Too bad!  The word was %s' % random_word.upper())
	
		else:
			if try_guess(guess):
				print('You got it!  The word was %s' % random_word.upper())

				correct = True
	
			else:
				print('Try again!')

	replay = input('Another word?  "Y" or "N": ').upper()
	
	while replay not in ['Y','N']:
		replay = (input('Please choose "Y" or "N": ').upper())

	if replay == 'N':
		print('Thanks for playing!')
		new_word = False
