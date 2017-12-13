# This is supposed to test teh source code. We should get back a True or False statement

from src.sudoku import Cell
# imports the cell
# test out creating Cell object

my_cell = Cell(1, 2)
# row and column of the cell. 1 and 2 are the arguments

passed = type(my_cell) == Cell
print("created Cell object, success: {}".format(passed))
# puts passed into the curly brackets

possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# These are our possible numbers
my_cell.set_possible_numbers(possible)
# .set is called a "method"
passed = my_cell.possible_numbers == possible
print('set possible number, success: {}'.format(passed))

# Test try new number
my_cell.try_new_number()
passed = my_cell.number != 0
# passed = true or false
print('try new number, success: {}'.format(passed))

# Test reset number to 0
my_cell.reset_number()
passed = my_cell.number == 0
# Tested if the function actually changed the number to 0
print('reset number to 0, success {}'.format(passed))

# Test exhaustion flag
while not my_cell.exhausted:
	# Checks if exhausted is false
	my_cell.try_new_number()
	# While it is not exhausted, keep trying new number
	# This loop is to make the code loop through all the numbers so that it would exhaust
passed = my_cell.exhausted
print('cell exhaustion success: {}'.format(passed))

# Test complete reset of cell except for position
my_cell.reset()
passed = not my_cell.number and not my_cell.possible_numbers and not my_cell.exhausted
# True = 1 and False = anything but 1
# not my_cell.number
print('Complete Reset success: {}'.format(passed))