from os import system, name

positions = [
			[1,2,3],
			[4,5,6],
			[7,8,9]
		]

board = [
			[0,0,0],
			[0,0,0],
			[0,0,0]
		]
"""
			[1,0,0],
			[0,-1,-1],
			[0,0,1]
"""

def cls():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_figure(value, position):
	match value:
		case -1:
			return '[O]'
		case 0:
			#return '[{}]'.format(positions[position[0]][position[1]])
			return '[{}]'.format((position[0]*3)+position[1]+1)

		case 1:
			return '[X]'

def print_board():
	print("")
	for idxr,r in enumerate(board):
		print(" ", end="")
		for idxc, c in enumerate(r):
			print("{}".format(get_figure(c, (idxr,idxc))), end="")
		print("")

def player_choice():
	while True:
		player_input = input("Jugador X, ingrese la posición elegida: ")
		if len(player_input) == 1 and player_input.isnumeric():
			break
		else:
			print("Jugador X debe elegir una posición")
			continue

cls()
print_board()
print("")
player_choice()
