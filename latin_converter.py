	#initial_word = input("Enter a word: \n->")
	#word = initial_word.lower()
def piglatin_converter(word):
	vowel = set('aeiou')
	if word[0] in vowel:
		latin_word = word + 'way'
		return (latin_word)
	elif vowel and set(word):
		while word[0] not in vowel:
			word = word[1:] + word[0]
			final_word = word +'ay'
		return(final_word)

#latin_Converter('andela')		