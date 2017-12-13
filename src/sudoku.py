# Miggy Reyes
# Computer Science Major at Texas Tech University
# Last updated on 11/9/2017

# we have Cells, Squares, Rows and columns
# We need to create a cell object
# 0 means no number in a cell
from time import time


class Cell(object):

	def __init__(self, row, column):
		# Creates a cell object and gives it position on the board
		self.row = row
		self.column = column
		self.number = 0
		self.possible_numbers = {}
		# you can also put set()
		self.exhausted = False
		# If you have tried all the possible numbers...
	#   It's false because we haven't

	def try_new_number(self):

		self.number = self.possible_numbers.pop()
		# Taking the number out of the possible numbers list and puts it in number

		if len(self.possible_numbers) == 0:
			# after popping possible numbers enough,
			# you are going to run out of numbers to pop
			self.exhausted = True
			# Tells us that there no more numbers available

	def reset(self):
		# Resets the whole board
		self.exhausted = False
		self.possible_numbers = set()
		self.number = 0  # This is like we have never put anything into the cell

	def reset_number(self):  # Resets the number in the square
		self.number = 0  # Resets number to 0

	def set_possible_numbers(self, numbers):
		# Takes numbers from outside
		self.possible_numbers = numbers

		if len(self.possible_numbers) == 0:
			self.exhausted = True  # Tells us that there no more numbers available


class Board(object):

	def __init__(self):
		self.board = []
		for i in range(9):
			row = []
			for j in range(9):
				row.append((Cell(i, j)))
			self.board.append(row)

	@staticmethod
	def difference(numbers):
		"""
		Get the remaining sudoku numbers remaining. The sets are unordered
		"""
		sudoku_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
		diff = sudoku_numbers - set(numbers)
		return diff

	@staticmethod
	def validate(numbers):
		"""
		Checks to see if the board follows the rules of sudoku
		Removes all 0s
		"""
		sudoku_numbers = []
		for num in numbers:
			if num != 0:
				sudoku_numbers.append(num)

		# check if only correct numbers are left
		check_correct = set(sudoku_numbers).issubset(
			{1, 2, 3, 4, 5, 6, 7, 8, 9})
		# checks that there is no duplicate numbers
		check_duplicate = len(sudoku_numbers) == len(set(sudoku_numbers))
		# The board is valid if these are all true
		valid = check_correct and check_duplicate
		return valid

	def get_row(self, row):
		r = self.board[row]
		row_numbers = []
		for cell in r:
			cell_num = cell.number
			row_numbers.append(cell_num)
		return row_numbers

	def get_column(self, column):
		# get a column of numbers for the specified column
		column_numbers = []
		for row in range(9):
			col = self.board[row][column]
			# What does this mean/do???
			num = col.number
			column_numbers.append(num)
		return column_numbers

	def get_square(self, row, column):
		"""
		Get a 3x3 square of cells in the board that the specified cell belongs to.
		"""
		square = []
		# What does this range mean?
		for r in range(row - (row % 3), row + (3 - (row % 3))):
			for c in range(column - (column % 3), column + (3 - (column % 3))):
				cell = self.board[r][c]
				num = cell.number
				square.append(num)
		return square

	def is_valid(self):
		"""
		validates the columns
		"""
		column_valid = True
		for r in range(9):
			column = self.get_column(r)
			column_valid = self.validate(column)
			if not column_valid:
				# Found invalid column, exit loop
				break
		# Validates the rows
		row_valid = True
		for r in range(9):
			row = self.get_row(r)
			row_valid - self.validate(row)
			if not row_valid:
				break

		# validates all 3x3 squares
		square_valid = True
		# range (0,9,3) steps through the numbers
		# 0-9 in increments of 3... [0, 3, 6]
		for r in range(0, 9, 3):
			for c in range(0, 9, 3):
				square = self.get_square(r, c)
				square_valid = self.validate(square)
				if not square_valid:
					break
		return column_valid and row_valid and square_valid

	def possible_numbers(self, r, c):
		row = self.get_row(r)
		column = self.get_column(c)
		square = self.get_square(r, c)
		return self.difference(row + column + square)

	def clear(self):
		# resets all cells on the board
		for r in range(9):
			for c in range(9):
				self.board[r][c].reset()

	def __str__(self):
		pretty = ""
		for i in range(9):
			pretty += str(self.get_row(i))
			pretty += "\n"
		return pretty

	def solve(self):
		"""
		Solve a 9x9 Sudoku Puzzle by using Brute Force(backtracking).
		"""
		# Checks if the initial board is valid
		if self.is_valid():
			row = 0
			start = time()
			# Where is time function located
			attempted_cells = []
			while row < 9:
				column = 0
				while column < 9:
					cell = self.board[row][column]
					backtracking = False
					if not cell.number:
						# if the cells number is 0
						if not cell.exhausted and not cell.possible_numbers:
							possible = self.possible_numbers(row, column)
							cell.set_possible_numbers(possible)

						if cell.possible_numbers:
							cell.try_new_number()
							attempted_cells.append(cell)
						elif attempted_cells:
							backtracking = True
							cell.reset()
							prev_cell = attempted_cells.pop(-1)
							prev_cell.reset_number()

						else:
							return False, -1

					if not backtracking:
						column += 1
				row += 1
			end = time()
			return True, end - start
			# Check to see where "end" is

		else:
			return False, -1