def EulerovKon(chessboard_size):
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    position_x = 0
    position_y = 0

    chessboard = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]

    for x in range(8):
        for y in range(8):
            print(chessboard[x][y], end=" ")
        print("")

    checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move)


def checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move):
    layout = []
    for i in range(8):
        if moveValidation(position_x + x_move[i], position_y + y_move[i], chessboard_size):
            layout.append([position_x + x_move[i], position_y + y_move[i]])

    return layout


def moveValidation(position_x, position_y, chessboard_size):
    print("Validating position")
    if position_x < 0 or position_x >= chessboard_size or position_y < 0 or position_y >= chessboard_size:
        return False
    else:
        return True


def windstoffAlgorhithm():
    print("algo")


if __name__ == '__main__':
    print("Zadaj Veľkosť plochy: \n")
    chessboard_size = int(input())
    EulerovKon(chessboard_size);
