from os import system, name

def cls():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
"""
		positions = [
			[1,2,3],
			[4,5,6],
			[7,8,9]

			   1 	 2 	   3
			[(0,0),(0,1),(0,2)],
			   4 	 5 	   6
			[(1,0),(1,1),(1,2)],
			   7 	 8 	   9
			[(2,0),(2,1),(2,2)]


			   3 	 4 	   5
			[(0,0),(0,1),(0,2)],
			   6 	 7 	   8
			[(1,0),(1,1),(1,2)],
			   9 	 10	   11
			[(2,0),(2,1),(2,2)]
		]
"""
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
		self.playing = True

	def start(self):
		while self.playing:
			self.step()

	def step(self):
		cls()
		self.print_board()
		print("")
		self.player_choice()

	def __position2number(self,x, y):
		return x*3 + y + 1

	def __number2position(self, number):
		x = ((number + 2) // 3 ) -1
		y = (number + 2) % 3
		return { 'x':x, 'y':y}

		"""
x*3 + y + 1 = position

x = (position // 3 ) -1

y = position+2 % 3

		"""

	def change_player(self):
		if self.current_player == 1:
			self.current_player = -1
		else:
			self.current_player = 1

	def __get_current_player_symbol(self):
		return self.get_symbol(self.current_player)

	def get_symbol(self, value, position=None):
		match value:
			case -1:
				return '\033[94m\033[01m[O]\033[00m'
			case 0:
				#return '[{}]'.format(positions[position[0]][position[1]])
				#return '\033[90m[{}]\033[00m'.format((position[0]*3)+position[1]+1)
				return '\033[90m[{}]\033[00m'.format(self.__position2number(*position))

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
		cls()
		self.print_board()
		print("")
		if winner == 2:
			print("Partida empatada")
		else:
			print("Ganó el jugador {}".format(self.__get_current_player_symbol()))

	def player_choice(self):
		while True:
			player_input = input("Jugador {}, ingrese la posición elegida: ".format(self.__get_current_player_symbol()))
			if len(player_input) == 1 and player_input.isnumeric():
				position = self.__number2position(int(player_input))
				#print("Position {}".format(position))
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
					print("Jugador {} debe elegir una posición válida.".format(self.__get_current_player_symbol()))
					continue					
			else:
				print("Jugador {} debe elegir una posición válida".format(self.__get_current_player_symbol()))
				continue

game = Game()
game.start()