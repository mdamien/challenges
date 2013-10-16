#Some live coding done during the phone interview

#sudoku verifier

def verify_uniqueness(arr):
	stripped_arr = [x for x in arr if x != ' ']
	return len(stripped_arr) == len(set(stripped_arr))
def verify(grid):
	#horizontal lines
	for line in grid:
		if not verify_uniqueness(line):
			return False
	#vertical lines
	for line in zip(*grid): #transpose the grid
	if not verify_uniqueness(line):
		return False
	#blocks
	for i in range(3):
        for j in range(3):
			block = sum([[grid[y][x] for x in range(i,i+3)] for y in range(j,j+3)])
			if not verify_uniqueness(block):
				return False
	return True
	
"""
General binary tree serialize | unserializer
   1
  | |
 2  7  
   | |
   9 10
     |
     2 
"(1R(2)L(7R(9)L(10L(2))))" -> (rootRrightLleft)

"""
def serialize(tree):
	s = "("+str(tree.value)
	if tree.right:
		s += "R"+serialize(tree.right)
	if tree.left:
			s += "L"+serialize(tree.left)
	return s+")"
class Node:
	def __init__(self,value,left,right):
		self.value = value
		self.left = left
		self.right = right

def unserialize(s):
	lnode,rnode = None,None
	end = s.rfind(")")
	if 'L' in s:
		lpos = s.find("L")
        node = unserialize(s[lpos:end])
        end = lpos
    if 'R' in s:
		rpos = s.find("R")
		node =unserialize(s[rpos:end])
        end = rpos
    return Node(s[1:end],lnode,rnode)
