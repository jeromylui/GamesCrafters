class gameTree:
	def __init__(self, position, move=None, parent = None, branches=[]):
		self.position = position
		for branch in branches:
			assert isinstance(branch, gameTree)
		self.parent = parent
		self.branches = branches
		self.status = "Undecided"
		self.move = move
		self.turn = True #True if curr player's turn. False otherwise.

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

	def addBranch(self, branch):
		assert isinstance(branch, gameTree)

	def changeBranches(self, branches = []):
		for branch in branches:
			assert isinstance(branch, gameTree)
		self.branches = branches


	def getStatus(self):
		return self.status

	def gameMove(self, moved):
		self.turn = not self.turn
		return self.move(self.position, moved)

	def changeStatus(self, status):
		assert status == "Win" or status == "Loss" or status == "Tie" or status == "Undecided"
		self.status = status

#----------------------------------------------------
def initial_position():
	return 3

def primitive(pos):
	if pos <= 0:
		return True
	else:
		return False

def gen_moves(pos):
	possible = []
	if pos-1 >= 0:
		possible += [1]
	if pos-2 >0 :
		possible += [2]
	return possible
	
def do_moves(pos, move):
	return pos-move

#----------------------------------------------------

def simplesolver(init, prim, gen, do):
	game = gameTree(init(), do)
	possible_moves = gen(game.getPosition())
	for pos in possible_moves: #[1,2]
		if prim(game.getPosition() - pos):
			if game.turn:
				game.changeStatus("Win")
			break
		return simplesolver(lambda: game.gameMove(pos), prim, gen, do)

	if game.getStatus == "Undecided":
		game.changeStatus("Loss")
		
	return game.getStatus()

print(simplesolver(initial_position, primitive, gen_moves, do_moves))