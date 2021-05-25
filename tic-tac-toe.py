#classic tic tac toe
board={'7':' ','8':' ','9':' ',
       '4':' ','5':' ','6':' ',
       '1':' ','2':' ','3':' '} 
board_k = []
for key in board:
	board_k.append(key)
#print(board)		#the board

def printedboard(board):
	print (board['7'] , '|' , board['8'] , '|' , board['9'])
	print('--+---+--')	
	print (board['4'] , '|' , board['5'] , '|' , board['6'])
	print('--+---+--')	
	print (board['1'] , '|' , board['2'] , '|' , board['3'])

#printedboard(board)

def game():
	count=0
	turn='X'

	for i in range(10):
		printedboard(board)
		print("Its you turn " , turn, "where you want to mark?")
		move=input()

		if board[move]==' ':
			board[move]=turn
			count=count+1
			print(count)
		else:
			print("the place to be marked is already filled. ")
			continue

		if count >= 5:
			if board['9'] == board['5'] == board['1'] !=' ':			#the Diaonal from right hand side
				printedboard(board)
				print("\nThe Game is over\n")
				print("The Game is Won by\n ", turn)
				break
			elif board['7'] == board['5'] == board['3'] !=' ':		#the Diagonal from left hand side
				printedboard(board)
				print("\nThe Game is over.\n" )
				print("The Game is Won by\n", turn)
				break
			elif board['7'] == board['8'] == board['9'] !=' ':		#the top from either side
				printedboard(board)
				print("\nThe Game is over.\n" )
				print("The Game is Won by\n", turn)
				break
			elif board['4'] == board['5'] == board['6'] !=' ':		#the middle one from either side
				printedboard(board)
				print("\nThe Game is over.\n" )
				print("The Game is Won by\n", turn)
				break
			elif board['1'] == board['2'] == board['3'] !=' ':		#the bottom one from either side
				printedboard(board)
				print("\nThe Game is over.\n" )
				print("The Game is Won by\n", turn)
				break
			elif board['7'] == board['4'] == board['1'] !=' ':		#the left one from top or bottom
				printedboard(board)
				print("\nThe Game is over.\n" )
				print("The Game is Won by\n", turn)
				break
			elif board['8'] == board['5'] == board['2'] !=' ':		#the middle one from top or bottom
				printedboard(board)
				print("\nThe Game is over.\n" )
				print("The Game is Won by\n", turn)
				break
			elif board['9'] == board['6'] == board['3'] !=' ':		#the right one from top or bottom
				printedboard(board)
				print("\nThe Game is over.\n" )
				print("The Game is Won by\n", turn)
				break
		if count == 9:
			print("The Game is a tie. Its over\n")

		if turn == 'X':
			turn='O'
		else:
			turn='X'


	play_again = input("Do want to play Again?(y/n)")		#do make the player play agian
	if play_again == "Y" or play_again == "y":
		for key in board_k:#key
			board[key] = " "

		game()

if __name__ == "__main__":
    game()






