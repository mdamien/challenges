def get_words():
	return "sheep people inside job wake conspiracy".split()
 
"Insert the word inside the tree-dictionnary as a leaf with a key set as None"
def insert(dico, word):
	d = dico
	for letter in word.lower():
		if letter not in d:
			d[letter] = {}
		d = d[letter]
	d[None] = word
 
"Build the dictionnary as a K-tree of dict. The childs are the possible next letter"
def build_dict(words):
	dico = {}
	for word in words:
		insert(dico,word)
	return dico
 
"""Return the corrected word or None if no word matched
dico is the sub-tree containing the possibilities of next letter
goal is the su-string to match to a word in dico"""
def correct(dico,goal,prev=None):
	if goal == '' and None in dico:
			return dico[None]
	if goal != '':
		if goal[0] in dico: #try to find an exact match
			r = correct(dico[goal[0]], goal[1:],goal[0])
			if r: return r
        if goal[0] in "aeiouy": #try all vowels
            for v in "aeiouy":
                if v != goal[0] and v in dico:
                    r = correct(dico[v], goal[1:],goal[0])
                    if r: return r
        if prev and goal[0] == prev: #ignore repeated letters
            r = correct(dico, goal[1:],goal[0])
            if r: return r
 
if __name__ == "__main__":
	dico = build_dict(get_words())
	try:
		while True:
			word = raw_input(">")
			r = correct(dico,word.lower())
			if r:
				print r
			else:
				print "NO SUGGESTION"
	except KeyboardInterrupt:
		pass
