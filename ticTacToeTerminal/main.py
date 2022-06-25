"""
Goals:
- Add AI
- Give it logic (cannot put a slot where there already has a piece) (DONE)
- decide who win (DONE)
"""

ticTacToe = [ [" " for _ in range(3)] for _ in range (3)]
turn = "o"
win = False

#who tf needs readability LOL
while (False if True not in [True if " " in ticTacToe[x] else False for x in range(len(ticTacToe))] else True) or win:
    if ticTacToe[int((x := input("enter coordinates (x, y) (start from 0)"))[1])][int(x[0])] == " ": ticTacToe[int(x[1])][int(x[0])] = (turn := "o" if turn == "x" else "x")
    print(f"{ticTacToe[0][0]}|{ticTacToe[0][1]}|{ticTacToe[0][2]}\n{'-'*5}\n{ticTacToe[1][0]}|{ticTacToe[1][1]}|{ticTacToe[1][2]}\n{'-'*5}\n{ticTacToe[2][0]}|{ticTacToe[2][1]}|{ticTacToe[2][2]}")
    rotateTicTacToe = [[ticTacToe[0][0], ticTacToe[1][0], ticTacToe[2][0]], [ticTacToe[0][1], ticTacToe[1][1], ticTacToe[2][1]], [ticTacToe[0][2], ticTacToe[1][2], ticTacToe[2][2]]] #use zip(*upack) if you want. but it needs two lines so this is good enough
    for z in [rotateTicTacToe, ticTacToe]:
        for y in z:
            if len(set(y)) == 1 and y[0] != " " or z[0][0] == z[1][1] == z[2][2] != " " or z[0][2] == z[1][1] == z[0][2] != " ": print(f"WINNER:{turn}"); quit() 

