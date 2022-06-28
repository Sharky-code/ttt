import minimaxCodeIFoundInG4G as yes
ticTacToe = [ [" " for _ in range(3)] for _ in range (3)]
turn , win = "o", False
yes.opponent, yes.player = "o", "x" #doesn't work when flipped currently
if yes.opponent == "x": ticTacToe[(botMove := yes.findBestMove(ticTacToe))[0]][botMove[1]] = "o" if turn == "x" else "x"
print(f"{ticTacToe[0][0]}|{ticTacToe[0][1]}|{ticTacToe[0][2]}\n{'-'*5}\n{ticTacToe[1][0]}|{ticTacToe[1][1]}|{ticTacToe[1][2]}\n{'-'*5}\n{ticTacToe[2][0]}|{ticTacToe[2][1]}|{ticTacToe[2][2]}\nIt is {turn}'s turn")
while (False if True not in [True if " " in ticTacToe[x] else False for x in range(len(ticTacToe))] else True) or win:
	while ticTacToe[int((x := input("enter coordinates (x, y) (start from 0)"))[1])][int(x[0])] != " ": print("Try again")
	ticTacToe[int(x[1])][int(x[0])] = turn
	rotateTicTacToe = [[ticTacToe[0][0], ticTacToe[1][0], ticTacToe[2][0]], [ticTacToe[0][1], ticTacToe[1][1], ticTacToe[2][1]], [ticTacToe[0][2], ticTacToe[1][2], ticTacToe[2][2]]] #not gonna use zip(*unpackthing) cause unnessesary
	#if yes.opponent == "x": turn = "o" if turn == "x" else "x"
	ticTacToe[(botMove := yes.findBestMove(ticTacToe))[0]][botMove[1]] = "o" if turn == "x" else "x"
	print(f"{ticTacToe[0][0]}|{ticTacToe[0][1]}|{ticTacToe[0][2]}\n{'-'*5}\n{ticTacToe[1][0]}|{ticTacToe[1][1]}|{ticTacToe[1][2]}\n{'-'*5}\n{ticTacToe[2][0]}|{ticTacToe[2][1]}|{ticTacToe[2][2]}\nIt is {turn}\'s turn")
	for z in [rotateTicTacToe, ticTacToe]: #try and compact this because I hate readability
		for y in z:
			if len(set(y)) == 1 and y[0] != " " or z[0][0] == z[1][1] == z[2][2] != " " or z[0][2] == z[1][1] == z[2][0] != " ": print(f"WINNER:{'o' if turn == 'x' else 'x'}"); quit() 
print("tie")
