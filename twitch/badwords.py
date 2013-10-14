"Generate bad words and test them against the spellcheck program"
import random

def mess_it_up(word):
	word = list(word)
	#mess the vowels
	for i,l in enumerate(word):
		if l in "aeiouy" and random.random() > 0.4:
			word[i] = random.choice("aeiouy")
	#add repeated letters
	for i,l in enumerate(word):
		if random.random() > 0.7:
			n = random.randint(1,4)
			word = word[:i]+[word[i]]*n+word[i+1:]
	#mess the casing
	for i,l in enumerate(word):
		if random.random() > 0.7:
			word[i] = l.swapcase()
	return "".join(word)

words = "sheep people inside job wake conspiracy".split()
for i in xrange(20):
	print mess_it_up(random.choice(words))
