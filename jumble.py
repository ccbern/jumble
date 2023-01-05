import requests
import random

word_list = []
pared_word_list = []
new_word = True

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
words = response.content.splitlines()

for w in words:
	word_list.append(w.decode('ASCII'))

min_word_length = int(input('Minimum word length: '))
max_word_length = int(input('Max word length: '))

for word in word_list:
	if len(word) >= min_word_length and len(word) <= max_word_length:
		pared_word_list.append(word)

while new_word:
	guess = 'first'
	random_order = []
	random_word_num = random.randrange(len(pared_word_list))
	random_word = pared_word_list[random_word_num]

	pared_word_list.remove(random_word)
	# print(random_word)

	word_to_break = random_word
	
	for letter in word_to_break:
		random_let_num = random.randrange(len(word_to_break))
		random_letter = word_to_break[random_let_num]
		word_to_break = word_to_break.replace(random_letter,'',1)
		random_order.append(random_letter)

	random_order_string = ''.join(random_order)

	print(random_order_string)

	if guess == 'first':
		guess = input('First guess: ').lower()
		# print(guess)
		# print(random_word)
	
	while guess != random_word:
		print(random_order_string)
		guess = input('Not right!  Guess again!: ').lower()

		# print(guess)
		# print(random_word)

	print('You got it!  The word was %s' % random_word.upper())

	replay = input('Another word?  "Y" or "N": ').upper()
	
	while replay not in ['Y','N']:
		replay = (input('Please choose "Y" or "N": ').upper())

	if replay == 'N':
		print('Thanks for playing!')
		new_word = False
