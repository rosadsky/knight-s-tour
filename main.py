def EulerovKon(chessboard_size):
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]
    starting_position_x = 0
    starting_position_y = 0

    chessboard = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]



    #checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move)
    windstoffAlghorhithm(starting_position_x,starting_position_y,chessboard,x_move, y_move,chessboard_size)

def checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move,chessboard):
    layout = []
    for i in range(8):
        #print("X: " + str(position_x + x_move[i]), "Y : " + str(position_y+ y_move[i]))
        if moveValidation(position_x + x_move[i], position_y + y_move[i], chessboard_size,chessboard):
            layout.append([position_x + x_move[i], position_y + y_move[i]])
    return layout

def moveValidation(position_x, position_y, chessboard_size,chessboard):
    #print("Validating position -> " + str(position_x) + " | " + str(position_y))

    if position_x >= 0 and position_x < chessboard_size and position_y >= 0 and position_y < chessboard_size and chessboard[position_x][position_y] == 0:
        print("VALID: " + str(position_x) +  " AND " + str(position_y))
        return True
    else:
        return False

def printChessboard(chessboard):
    for x in range(8):
        for y in range(8):
            print(chessboard[x][y], end=" ")
        print("")

def windstoffAlghorhithm(starting_position_x,starting_position_y,chessboard,x_move, y_move,chessboard_size):
    position_x = starting_position_x
    position_y = starting_position_y

 #   positions = checkHorseInChessboard(chessboard_size,position_x,position_y,x_move,y_move,chessboard)
    positions = checkHorseInChessboard(chessboard_size, 0, 0 , x_move, y_move, chessboard)
    #print(positions)
    minimum = []
    moves_counter = 0


    for possible_move in positions:
        print("MOVE:")
        print(possible_move)
        possible_move_positions = checkHorseInChessboard(chessboard_size,possible_move[0],possible_move[1],x_move,y_move,chessboard)
        print("PMP:")
        print(possible_move_positions)

        if(len(minimum) > len(possible_move_positions) or len(minimum) == 0):
            minimum = possible_move

    moves_counter =+ 1
    print(minimum)
    position_x = minimum[0]
    position_y = minimum[1]
    chessboard[position_x][position_y] = moves_counter

    #printChessboard(chessboard)

    print("FINAL MINIMUM")
    print(minimum)











if __name__ == '__main__':
    print("Zadaj Veľkosť plochy: \n")
    chessboard_size = int(input())
    EulerovKon(chessboard_size)
