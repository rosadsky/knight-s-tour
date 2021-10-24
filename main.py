import time



def EulerSolve(chessboard_size):
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    print("Insert the X position of starting point from 0 - " + str(chessboard_size - 1) )
    starting_position_x = int(input())
    print("Insert the Y position of starting point from 0 - " + str(chessboard_size - 1) )
    starting_position_y = int(input())

    chessboard = [[-1 for i in range(chessboard_size)] for j in range(chessboard_size)]


    #checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move)
    windstoffAlgorithm(starting_position_x,starting_position_y,chessboard,x_move, y_move,chessboard_size)

def checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move,chessboard):
    layout = []
    for i in range(8):
        #print("X: " + str(position_x + x_move[i]), "Y : " + str(position_y+ y_move[i]))
        if moveValidation(position_x + x_move[i], position_y + y_move[i], chessboard_size,chessboard):
            layout.append([position_x + x_move[i], position_y + y_move[i]])
    return layout

def moveValidation(position_x, position_y, chessboard_size,chessboard):

    if position_x >= 0 and position_x < chessboard_size and position_y >= 0 and position_y < chessboard_size and chessboard[position_x][position_y] == -1:
        #print("VALID: " + str(position_x) +  " AND " + str(position_y))
        return True
    else:
        return False

def printChessboard(chessboard,chessboard_size):
    for x in range(chessboard_size):
        for y in range(chessboard_size):
            print(chessboard[x][y], end=" ")
        print("")

def windstoffAlgorithm(starting_position_x,starting_position_y,chessboard,x_move, y_move,chessboard_size):
    position_x = starting_position_x
    position_y = starting_position_y

    start = time.time_ns()

    moves_counter = 1

    chessboard[position_x][position_y] = moves_counter

    iterations = chessboard_size * chessboard_size - 1

    for x in range(iterations):
        positions = checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move, chessboard)
        if(len(positions) == 0):
            print("NO SOLUTION FOR THIS INPUT TRY ANOTHER ONE")
            break
        minimum = positions[0]

        for possible_move in positions:
            possible_move_positions = checkHorseInChessboard(chessboard_size,possible_move[0],possible_move[1],x_move,y_move,chessboard)
            possible_minimum = checkHorseInChessboard(chessboard_size,minimum[0],minimum[1],x_move,y_move,chessboard)

            if(len(possible_minimum) >= len(possible_move_positions) or len(minimum) == 0):
                minimum = possible_move

        moves_counter += 1
        position_x = minimum[0]
        position_y = minimum[1]
        chessboard[position_x][position_y] = moves_counter


        #printChessboard(chessboard,chessboard_size)
        #print("MOVE NO. " + str(moves_counter))
        #print("-------------------------")



    printChessboard(chessboard,chessboard_size)
    end = time.time_ns()
    total_time = end - start
    print("------------------------")
    print("TOTAL MOVES " + str(moves_counter))
    print("TOTAL TIME: " + str(total_time/1000000) + " milliseconds..")
    if(finalCheck(chessboard,chessboard_size) == False):
        print("NO SOLUTION")


def solveDPS(chessboard_size,chessboard,position_x,position_y,x_move,y_move, iteration):
    if (iteration == chessboard_size ** 2):
        return True

    for i in range(8):
        new_postion_x = position_x + x_move[i]
        new_postion_y = position_y + y_move[i]
        if (moveValidation(new_postion_x, new_postion_y, chessboard_size , chessboard)):
            chessboard[new_postion_x][new_postion_y] = iteration
            print("MOVE: " + str(chessboard[new_postion_x][new_postion_y]))

            if (solveDPS(chessboard_size,chessboard,position_x,position_y,x_move,y_move, iteration + 1)):
                return True

            # Backtracking
            #print("BACKTRACKING: " + str(board[new_x][new_y]))
            chessboard[new_postion_x][new_postion_y] = -1


    return False

def finalCheck(chessboard,chessboard_size):

    checkmark = True
    for i in range(chessboard_size):
        for j in range(chessboard_size):
            if(chessboard[i][j] == 0):
                checkmark = False

    return checkmark


if __name__ == '__main__':
    print("Insert size of chessboard X: \n")
    chessboard_size = int(input())
    EulerSolve(chessboard_size)
