"""
Interactive spellchecker for twitch.tv spellcheck challenge
"""

"Insert the word inside the tree-dictionnary as a leaf with a key set as None"
def insert(dic, word):
	d = dic
	for letter in word.lower():
		if letter not in d:
			d[letter] = {}
		d = d[letter]
	d[None] = word

"Build the dictionnary as a K-tree of dict. The childs are the possible next letter"
def build_dic():
	dic = {}
	for word in open('/usr/share/dict/words','r'):
		insert(dic,word.strip())
	return dic

"""Return the corrected word or None if no word matched
dic is the sub-tree containing the possibilities of next letter
goal is the su-string to match to a word in dic"""
def correct(dic,goal,prev=None):
	if len(goal) == 0 and None in dic: #return if an exact match is found
			return dic[None]
	elif len(goal) > 0:
		if goal[0] in dic: #try to find an exact match
			r = correct(dic[goal[0]], goal[1:],goal[0])
			if r: return r
		if goal[0] in "aeiouy": #try all vowels
			for v in "aeiouy":
				if v != goal[0] and v in dic:
					r = correct(dic[v], goal[1:],goal[0])
					if r: return r
		if prev and goal[0] == prev: #ignore repeated letters
			r = correct(dic, goal[1:],goal[0])
			if r: return r

if __name__ == "__main__":
	dic = build_dic()
	try:
		while True:
			word = raw_input(">")
			r = correct(dic,word.lower())
			if r:
				print r
			else:
				print "NO SUGGESTION"
	except (KeyboardInterrupt,EOFError):
		pass
