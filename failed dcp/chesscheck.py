import random


def generate_board():
	board = []
	for i in range(8):
		board.append([])
		for e in range(4):
			if i % 2 == 0: # i is an even number
				board[i].append("#")
				board[i].append(" ")
			else:
				board[i].append(" ")
				board[i].append("#")
	return board


def print_board(board_):
	for row in board_:
		row_ = "|"
		for cell in row:
			row_ += f"{cell}|"
		print(row_)


def add_pieces(board_):
	occupied = []
	# add black king
	king_x = random.randint(0, 7)
	king_y = random.randint(0, 7)
	board_[king_y][king_x] = "K"
	occupied.append([king_x, king_y, "K"])

	# add white pieces
	# R = rook
	# N = knight
	# B = bishop
	# P = pawn
	pieces = ["R", "N", "B", "Q", "P"]
	for p in pieces:
		while True:
			not_occupied = True
			piece_x = random.randint(0, 7)
			piece_y = random.randint(0, 7)
			# check if x and y are occupied
			for xy in occupied:
				if xy[0] == piece_x:
					if xy[1] == piece_y:
						not_occupied = False
			if not_occupied:
				occupied.append([piece_x, piece_y, p])
				break
		# add piece to board
		board_[piece_y][piece_x] = p
	return occupied


def checkifcheck(board_, pieces):
	king_x = pieces[0][0]
	king_y = pieces[0][1]
	checked = False
	for p in pieces:
		
		if p[2] == "R":
			if king_x == p[0] or king_y == p[1]:
				checked = True
			'''
			if king_x == p[0]:
				if king_x > p[0]:
					# search if blocked from below 
					for pi in pieces
				else: 
					# search if blocked from above
					for pi in pieces:
						if pi[2] > king_x:
							checked = True
			if king_y == p[1]:
				checked = True
			'''

		elif p[2] == "N":
			if king_x-2 == p[0] or king_x+2 == p[0]:
				if king_y-1 == p[1] or king_y+1 == p[1]:
					checked = True
			elif king_x-1 == p[0] or king_x+1 == p[0]:
				if king_y-2 == p[1] or king_y+2 == p[1]:
					checked = True

		elif p[2] == "B":
			# chech if king is in diagonal lines
			for i in range(7):
				if p[0]+i == king_x or p[0]-i == king_x:
					if p[1]+i == king_y or p[1]-i == king_y:
						checked = True

		elif p[2] == "Q":
			# horizontal and vertical line
			if king_x == p[0] or king_y == p[1]:
				checked = True
				break
			# diagonal lines
			for i in range(7):
				if p[0]+i == king_x or p[0]-i == king_x:
					if p[1]+i == king_y or p[1]-i == king_y:
						checked = True
		
		elif p[2] == "P":
			if king_y == p[1]-1:
				if king_x == p[0]-1 or king_x == p[0]+1:
					checked = True
		
		if checked == True:
			break
	return checked


def main():
	chess_board = generate_board()
	pieces_list = add_pieces(chess_board)
	print(pieces_list)
	print(checkifcheck(chess_board, pieces_list))
	print_board(chess_board)


main()
