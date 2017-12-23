from os import path, listdir, mkdir

""" 
Writes and Reads the Sudoku Board
"""

# Does this make a working directory no matter where it is?
DATA_DIR = "../data/"


def ensure_data_dir():
	# Checks to see if there is a directory made
	data_dir = path.normpath(DATA_DIR)
	if not path.isdir(data_dir):
		mkdir(data_dir)


def write(board):
	ensure_data_dir()
	f_path = ""
	try:
		name = DATA_DIR + 'saved-board'
		number = len(listdir(DATA_DIR))
		name += str(number) + ".txt"
		file = open(name, 'w')
		out = ""
		for r in range(9):
			for c in range(9):
				cell = board.board[r][c]
				number = cell.number
				out += str(number)
		file.write(out)
		f_path = name
		file.close()
	except FileNotFoundError as e:
		print(e)
	return f_path
