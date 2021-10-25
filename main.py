import time

steps_program = 1

def EulerSolve(chessboard_size):
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    print("Insert the X position of starting point from 0 - " + str(chessboard_size - 1) )
    starting_position_x = int(input())
    print("Insert the Y position of starting point from 0 - " + str(chessboard_size - 1) )
    starting_position_y = int(input())

    chessboard = [[-1 for i in range(chessboard_size)] for i in range(chessboard_size)]


    chessboard[starting_position_x][starting_position_y] = 0

    iteration = 1

    #checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move)
    #windstoffAlgorithm(starting_position_x,starting_position_y,chessboard,x_move, y_move,chessboard_size)
    start = time.time_ns()

    if (solveDPS(chessboard_size,chessboard,starting_position_x,starting_position_y,x_move,y_move, iteration)):
        printChessboard(chessboard,chessboard_size)
    else:
        print("NO SOLUTUTION FOR THIS INPUT")

    end = time.time_ns()
    total_time = end - start
    print("------------------------")
    print("TOTAL ATTEMPTS " + str(steps_program))
    print("TOTAL TIME: " + str(total_time / 1000000) + " milliseconds..")

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


def bubblesort(list,x_move,y_move,chessboard):
    for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
        first = checkHorseInChessboard(chessboard_size, list[idx][0], list[idx][1], x_move, y_move, chessboard)
        second = checkHorseInChessboard(chessboard_size, list[idx+1][0], list[idx+1][1], x_move, y_move, chessboard)
        if len(first)>len(second):
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
            #print("CHANGE")

    return list


def solveDPS(chessboard_size,chessboard,position_x,position_y,x_move,y_move, iteration):
    if (iteration == chessboard_size ** 2):
        return True

    global steps_program

    positions = checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move, chessboard)
    positions = bubblesort(positions,x_move,y_move,chessboard)

    for i in positions:
        new_postion_x = i[0]
        new_postion_y = i[1]

        steps_program += 1
        if steps_program == 10000000:
            return False

        if (moveValidation(new_postion_x, new_postion_y, chessboard_size , chessboard)):
            chessboard[new_postion_x][new_postion_y] = iteration

            #FINAL CHECK
            if (solveDPS(chessboard_size,chessboard,new_postion_x,new_postion_y,x_move,y_move, iteration + 1)):
                return True

            chessboard[new_postion_x][new_postion_y] = -1


    #print("FALSE")
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
