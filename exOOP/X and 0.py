board = [[" "]*3 for i in range(3)]

def draw_board():
    print()
    print("    | 0 | 1 | 2 |")
    print("-----------------")
    for i, row in enumerate(board):
        row_str = f"  {i} | {' | '.join(row)} |"
        print(row_str)
        print("-----------------")
    print()



def ask():
    while True:
        cords = input("   Твой ход - ").split()
        if len(cords) != 2:
            print("Введите две кординаты ")
            continue
        x,y = cords
        x,y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if board[x][y] == " ":
                return x, y
            else:
                print("Клетка занята!")
        else:
            print("Кординаты вне игры")

        return x,y

def win_check():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win:
        sym = []
        for cr in cord:
            sym.append(board[cr[0]][cr[1]])
        if sym == ["X","X","X"]:
            print("Выиграл Х")
            return True
        if sym == ["0","0","0"]:
            print("Выиграл 0")
            return True

    return False



count = 0
while True:
    count += 1
    draw_board()

    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x,y = ask()

    if count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if win_check():
        break
    if count == 9:

        print("НИЧЬЯ")
        break

