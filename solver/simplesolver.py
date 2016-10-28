class gameTree:
	def __init__(self, position, parent = None, branches=[]):
		self.position = position
		for branch in branches:
			assert isinstance(branch, gameTree)
		self.parent = parent
		self.branches = branches
		self.status = "Undecided"
		self.turn = False #True if curr player's turn. False otherwise.

	def __repr__(self):
		if self.branches:
			return 'gameTree({0}, {1})'.format(self.position, repr(self.branches))
		else:
			return 'gameTree({0})'.format(repr(self.position))

	def is_leaf(self):
		return not self.branches

	def getPosition(self):
		return self.position

	def getBranches(self):
		return self.branches

	def getTurn(self):
		return self.turn

	def hasParent(self):
		return self.parent != None

	def addBranch(self, branch):
		assert isinstance(branch, gameTree)
		self.branches += [branch]

	def changeBranches(self, branches = []):
		for branch in branches:
			assert isinstance(branch, gameTree)
		self.branches = branches


	def getStatus(self):
		return self.status

	def changeStatus(self, status):
		assert status == "Win" or status == "Loss" or status == "Tie" or status == "Undecided"
		self.status = status

#----------------------------------------------------
def initial_position():
	return 4

def primitive(pos):
	if pos <= 0:
		return True
	else:
		return False

def gen_moves(pos):
	possible = []
	if pos-2 >=0 :
		possible += [2]
	if pos-1 >= 0:
		possible += [1]
	return possible
	
def do_moves(pos, move):
	return pos-move

#----------------------------------------------------
def simplesolver(init, prim, gen, do):
	root = gameTree(init())
	def helper(init, prim, gen, do, game):
		nonlocal root
		if not game:
			game = gameTree(init())
		print(game)
		if game.parent:
			game.turn = not game.parent.turn
		if prim(game.getPosition()):
			if game.getTurn():
				return True
			return False
		possible_moves = gen_moves(game.getPosition())
		if (len(possible_moves) > 1) and prim(do(game.getPosition(), possible_moves[0])):
			possible_moves.pop()
		game.changeBranches([gameTree(do(game.getPosition(), move), game) for move in possible_moves])
		for branch in game.getBranches():
			if helper(init, prim, gen, do, branch) and not game.getTurn():
				root.changeStatus("Win")
	helper(init, prim, gen, do, None)
	if root.getStatus() == "Undecided":
		root.changeStatus("Loss")
	return root.getStatus()


print(simplesolver(initial_position, primitive, gen_moves, do_moves))
