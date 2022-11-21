from os import system, name

class Game:
	LINES = (
	    [(0, 0), (0, 1), (0, 2)], # Horizontal
	    [(1, 0), (1, 1), (1, 2)],
	    [(2, 0), (2, 1), (2, 2)],
	    [(0, 0), (1, 0), (2, 0)], # Vertical
	    [(0, 1), (1, 1), (2, 1)],
	    [(0, 2), (1, 2), (2, 2)],
	    [(0, 0), (1, 1), (2, 2)], # Diagonal
	    [(0, 2), (1, 1), (2, 0)],
	)

	def __init__(self):
		system('')
		self.current_player = 1
		self.board = [
			[0,0,0],
			[0,0,0],
			[0,0,0]
		]
		self.playing = False

	def start(self):
		self.playing = True
		while self.playing:
			self.step()

	def step(self):
		self.cls()
		self.print_board()
		print("")
		self.player_choice()

	def change_player(self):
		if self.current_player == 1:
			self.current_player = -1
		else:
			self.current_player = 1

	def get_current_player_symbol(self):
		return self.get_symbol(self.current_player)

	def get_symbol(self, value, position=None):
		match value:
			case -1:
				return '\033[94m\033[01m[O]\033[00m'
			case 0:
				return '\033[90m[{}]\033[00m'.format(self.position2number(*position))
			case 1:
				return '\033[91m\033[01m[X]\033[00m'

	def print_board(self):
		print("")
		for idxr,r in enumerate(self.board):
			print(" ", end="")
			for idxc, c in enumerate(r):
				print("{}".format(self.get_symbol(c, (idxr,idxc))), end="")
			print("")

	def check_result(self):
		for indexes in Game.LINES:
			row = [self.board[r][c] for r, c in indexes]
			if all(cell == 1 for cell in row):
				return 1
			if all(cell == -1 for cell in row):
				return -1
		for rows in self.board:
			for cell in rows:
				if cell == 0:
					return 0
		return 2

	def end(self, winner):
		self.cls()
		self.print_board()
		print("")
		if winner == 2:
			print("Partida empatada")
		else:
			print("Ganó el jugador {}".format(self.get_current_player_symbol()))

	def player_choice(self):
		while True:
			player_input = input("Jugador {}, ingrese la posición elegida: ".format(self.get_current_player_symbol()))
			if len(player_input) == 1 and player_input.isnumeric():
				position = self.number2position(int(player_input))
				if self.board[position['x']][position['y']] == 0:
					self.board[position['x']][position['y']] = self.current_player
					game_end = self.check_result()
					if game_end != 0:
						self.end(game_end)
						self.playing = False
					else:
						self.change_player()
					break
				else:
					print("Jugador {} debe elegir una posición válida.".format(self.get_current_player_symbol()))
					continue					
			else:
				print("Jugador {} debe elegir una posición válida".format(self.get_current_player_symbol()))
				continue
	
	def position2number(self,x, y):
		return x*3 + y + 1

	def number2position(self, number):
		x = ((number + 2) // 3 ) -1
		y = (number + 2) % 3
		return { 'x':x, 'y':y}

	def cls(self):
	    # for windows
	    if name == 'nt':
	        _ = system('cls')
	    # for mac and linux(here, os.name is 'posix')
	    else:
	        _ = system('clear')

game = Game()
game.start()