import time

global steps


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

    if (solveDPS(chessboard_size,chessboard,starting_position_x,starting_position_y,x_move,y_move, iteration)):
        printChessboard(chessboard,chessboard_size)
    else:
        print("RIEŠENIE NIEJE SHIT")

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

def bubblesort(list,x_move,y_move,chessboard):
   # print("SORTING")
    #print(list)
# Swap the elements to arrange in order
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




    #print(iteration)
    positions = checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move, chessboard)
    positions = bubblesort(positions,x_move,y_move,chessboard)
    #print(positions)
    #for check in positions:
        #print(len(checkHorseInChessboard(chessboard_size, check[0], check[1], x_move, y_move, chessboard)))



    for i in positions:
        new_postion_x = i[0]
        new_postion_y = i[1]
        #print("X: ["+ str(new_postion_x)+"] Y: [" + str(new_postion_y)+ "]")

        if (moveValidation(new_postion_x, new_postion_y, chessboard_size , chessboard)):
            chessboard[new_postion_x][new_postion_y] = iteration
            #print("MOVE: " + str(chessboard[new_postion_x][new_postion_y]) + "iteration " + str(i))
            #print("CHESSBOARD")
            #printChessboard(chessboard,chessboard_size)


            #FINAL CHECK
            if (solveDPS(chessboard_size,chessboard,new_postion_x,new_postion_y,x_move,y_move, iteration + 1)):
                print("DPS TRUE")
                return True

            # Backtracking
            print("BACKTRACKING: " + str(chessboard[new_postion_x][new_postion_y]) + " i: " + str(i))
            #printChessboard(chessboard, chessboard_size)
            chessboard[new_postion_x][new_postion_y] = -1
            #print("PO")
            #printChessboard(chessboard,chessboard_size)

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
