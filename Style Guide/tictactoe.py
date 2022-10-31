"""
	Description: This program allows the user to play multiple rounds of
	tic-tac-toe against the computer.
	Author: Mr. Bloom
	Date: Fall 2019
"""

import random

def display(board):
	""" This function prints out the board that it was passed.
		"board" is a list of 10 strings representing the board """
	print('\n ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
	print(' ---------')
	print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
	print(' ---------')
	print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])


def isSpaceFree(board, move):
	""" checks if space is open for the pending move """
	return board[move] == " "


def makeMove(board, move, letter):
	board[move] = letter
	return


def userTurn(board):
	while True:
		move = int(raw_input("  0-8: "))
		if move >= 0 and move <= 8:
			spaceFree = isSpaceFree(board, move)
			if spaceFree == True:
				makeMove(board, move, "x")
				return
			else:
				print("Sorry, that spot is taken. Please choose again.")
		else:
			print("Sorry, please choose a valid board location.")


def isWinner(bo, le):
	""" Given a board and a player's letter, this function returns True if that
		player has won. We use bo instead of board and le instead of letter
		 so we don't have to type as much. """

	if bo[6] == le and bo[7] == le and bo[8] == le:     # across the bottom
		PLAYERWON = True
	elif bo[3] == le and bo[4] == le and bo[5] == le:   # across the middle
		PLAYERWON = True
	elif bo[0] == le and bo[1] == le and bo[2] == le:   # across the top
		PLAYERWON = True
	elif bo[6] == le and bo[3] == le and bo[0] == le:   # down the left side
		PLAYERWON = True
	elif bo[7] == le and bo[4] == le and bo[1] == le:   # down the middle
		PLAYERWON = True
	elif bo[8] == le and bo[5] == le and bo[2] == le:   # down the right side
		PLAYERWON = True
	elif bo[6] == le and bo[4] == le and bo[2] == le:   # diagonal
		PLAYERWON = True
	elif bo[8] == le and bo[4] == le and bo[0] == le:   # diagonal
		PLAYERWON = True
	else:
		PLAYERWON = False

	return PLAYERWON


def isBoardFull(board):
	""" checks each space to see if it's empty. If empty string found, game continues """
	for i in range(9):
		if isSpaceFree(board, i):
			return False           # found an empty space so continue the game
	return True                    # never found an empty space, so must be a draw


def checkIfGameOver(board, letter):
	""" check if someone has won or a draw
		We use bo instead of board and le instead of letter so we don't have to type as much.
		return "x" if X wins, "o" if O wins, "d" if draw """

	winner = isWinner(board, letter)    # check to see if player X or O has won
	if winner == True:
		return letter                   # if so, return "x" or "o"
	else:                               # otherwise, no one has won yet...
		tieGame = isBoardFull(board)         # so check to see if the game is a draw
		if tieGame == True:
			return "d"              # never found an empty space, so must be a draw
		else:
			return None             # found an empty space so continue the game


def getBoardCopy(board):
	# Make a duplicate of the board list and return it the duplicate.
	dupeBoard = []
	for i in board:
		dupeBoard.append(i)
	return dupeBoard


def computerTurn(board):
	""" find best spot and play it """

	#------------- Here is my algorithm for our Tic Tac Toe AI:  -------------#

	# First, check if we can win in the next move
	for i in range(0, 9):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, i, "o")
			if isWinner(copy, "o"):
				makeMove(board, i, "o")
				return

	# Second, check if the player could win on their next move, and block them.
	for i in range(0, 9):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, i, "x")
			if isWinner(copy, "x"):
				makeMove(board, i, "o")
				return

	# Third, try to take the center, if it is free.
	if isSpaceFree(board, 4):
		makeMove(board, 4, "o")
		return

	# Fourth, try to take one of the corners, if they are free.
	while True:
		randMove = random.choice([0,2,6,8])
		if isSpaceFree(board, randMove):
			makeMove(board, randMove, "o")
			return

	# Fifth, move on one of the sides.
	while True:
		randMove = random.choice([1,3,5,7])
		if isSpaceFree(board, randMove):
			makeMove(board, randMove, "o")
			return


def main():
	""" run one game of tic-tac-toe """

	# print rules of game??
	board = [" "] * 9
	display(board)

	while True:
		userTurn(board)
		display(board)
		result = checkIfGameOver(board, "x")
		if result != None:
			break
		computerTurn(board)
		display(board)
		result = checkIfGameOver(board, "o")
		if result != None:
			break

	# game is over, print results
	if result == "x":
		print("X wins!")
	elif result == "o":
		print("O wins!")
	else:
		print("it's a draw....")


main()
