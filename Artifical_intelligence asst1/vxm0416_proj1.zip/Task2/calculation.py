import threading 

class Calculation:

    no_of_leafs_for_which_eval_is_called = 0

    def calculate(self, playBoard, presentTurn):

        dict1 = {0:0, 1:0, 2:0, 3:0, 4:0}
        dict2 = {0:0, 1:0, 2:0, 3:0, 4:0}
        self.getCounts(playBoard, 1, dict1)
        self.getCounts(playBoard, 2, dict2)
        result = (dict1[4] * 1000) + (dict1[3]*100) + (dict1[2]*10) + (dict1[1]*1) - (dict2[4]*1000) - (dict2[3]*100) - (dict2[2]*10) - (dict2[1]*1)
        self.no_of_leafs_for_which_eval_is_called += 1
        #print (self.no_of_leafs_for_which_eval_is_called)
        if presentTurn == 1:
            return result
        else:
            return -result

    def getScore(self, playBoard, player):

        playerScore = 0
        ignore_jcol = set()
        for i in range(5, -1, -1):
            if len(ignore_jcol) == 4:
                break 
            for j in range(6, 2, -1):
                if j in ignore_jcol:
                    continue
                elif playBoard[i][j] == 0:
                    ignore_jcol.add(j)
                    continue
                elif playBoard[i][j] == player and playBoard[i][j-1] == player and playBoard[i][j-2] == player and playBoard[i][j-3] == player:
                    playerScore += 1
        
        ignore_jcol = set()
        for i in range(5, 2, -1):
            if len(ignore_jcol) == 7:
                break
            for j in range(7):
                if j in ignore_jcol:
                    continue
                elif playBoard[i][j] == 0:
                    ignore_jcol.add(j)
                    continue
                elif playBoard[i][j] == player and playBoard[i - 1][j] == player and playBoard[i - 2][j] == player and playBoard[i - 3][j] == player:
                    playerScore += 1

        ignore_jcol = set()
        for i in range(5, 2, -1):
            if len(ignore_jcol) == 4:
                break
            for j in range(6, 2, -1):
                if j in ignore_jcol:
                    continue
                elif playBoard[i][j] == 0:
                    ignore_jcol.add(j)
                    continue
                elif playBoard[i][j] == player and playBoard[i - 1][j - 1] == player and playBoard[i - 2][j - 2] == player and playBoard[i - 3][j - 3] == player:
                    playerScore += 1

        ignore_jcol = set()
        for i in range(5, 2, -1):
            if len(ignore_jcol) == 4:
                break
            for j in range(4):
                if j in ignore_jcol:
                    continue
                elif playBoard[i][j] == 0:
                    ignore_jcol.add(j)
                    continue
                elif playBoard[i][j] == player and playBoard[i -1][j + 1] == player and playBoard[i -2][j + 2] == player and playBoard[i - 3][j + 3] == player:
                    playerScore += 1

        return playerScore


    def getCounts(self, playBoard, player, dict):

        ignore_jcol = set()
        for i in range(5, -1, -1):
            if len(ignore_jcol) >= 4:
                break
            for j in range(6, 2, -1):
                if j in ignore_jcol or j-1 in ignore_jcol or j-2 in ignore_jcol or j-3 in ignore_jcol:
                    if playBoard[i][j] == 0:
                        ignore_jcol.add(j)
                    if playBoard[i][j - 1] == 0:
                       ignore_jcol.add(j-1)
                    if playBoard[i][j - 2] == 0:
                        ignore_jcol.add(j-2) 
                    if playBoard[i][j - 3] == 0:
                        ignore_jcol.add(j-3)
                    continue
                if playBoard[i][j] != player and playBoard[i][j] != 0:
                    continue
                else:
                    count = 0
                    if playBoard[i][j] == player:
                        count += 1
                    elif playBoard[i][j] != 0:
                        continue
                    else:
                        ignore_jcol.add(j)
                    if playBoard[i][j - 1] == player:
                        count += 1
                    elif playBoard[i][j - 1] != 0:
                        j = j - 1
                        continue
                    else:
                        ignore_jcol.add(j - 1)
                    if playBoard[i][j - 2] == player:
                        count += 1
                    elif playBoard[i][j - 2] != 0:
                        j = j - 2
                        continue
                    else:
                        ignore_jcol.add(j - 2)
                    if playBoard[i][j - 3] == player:
                        count += 1
                    elif playBoard[i][j - 3] != 0:
                        j = j - 3
                        continue
                    else:
                        ignore_jcol.add(j - 3)
                    dict[count] += 1

        ignore_jcol = set()
        for i in range(5, 2, -1):
            if len(ignore_jcol) == 7:
                break
            for j in range(7):
                if playBoard[i][j] == 0:
                    ignore_jcol.add(j)
                    continue
                if j in ignore_jcol or playBoard[i][j] != player:
                    continue
                else:
                    if playBoard[i][j] == player and playBoard[i - 1][j] == player and playBoard[i - 2][j] == player and playBoard[i - 3][j] == player:
                        dict[4] += 1
                    elif playBoard[i][j] == player and playBoard[i - 1][j] == player and playBoard[i - 2][j] == player and       playBoard[i - 3][j] == 0:
                        dict[3] += 1
                    elif playBoard[i][j] == player and playBoard[i - 1][j] == player and playBoard[i - 2][j] == 0 and playBoard[i - 3][j] == 0:
                        dict[2] += 1
                    elif playBoard[i][j] == player and playBoard[i - 1][j] == player and playBoard[i - 2][j] == player and playBoard[i - 3][j] == 0:
                        dict[1] += 1
        
        ignore_jcol = set()
        for i in range(5, 2, -1):
            if len(ignore_jcol) >= 4:
                break
            for j in range(6, 2, -1):
                if j in ignore_jcol or j-1 in ignore_jcol or j-2 in ignore_jcol or j-3 in ignore_jcol:
                    if playBoard[i][j] == 0:
                        ignore_jcol.add(j)
                    if playBoard[i - 1][j - 1] == 0:
                        ignore_jcol.add(j-1)
                    if playBoard[i - 2][j - 2] == 0:
                        ignore_jcol.add(j-2)
                    if playBoard[i - 3][j - 3] == 0:
                        ignore_jcol.add(j-3)
                    continue
                if playBoard[i][j] != player and playBoard[i][j] != 0:
                    continue
                else:
                    count = 0
                    if playBoard[i][j] == player:
                        count += 1
                    elif playBoard[i][j] != 0:
                        continue
                    else:
                        ignore_jcol.add(j)
                    if playBoard[i - 1][j - 1] == player:
                        count += 1
                    elif playBoard[i - 1][j - 1] != 0:
                        j = j - 1
                        continue
                    else:
                        ignore_jcol.add(j - 1)
                    if playBoard[i - 2][j - 2] == player:
                        count += 1 
                    elif playBoard[i - 2][j - 2] != 0:
                        j = j - 2
                        continue
                    else:
                        ignore_jcol.add(j - 2)
                    if playBoard[i - 3][j - 3] == player:
                        count += 1
                    elif playBoard[i - 3][j - 3] != 0:
                        j = j - 3
                        continue
                    else:
                        ignore_jcol.add(j - 3)
                    dict[count] += 1


        ignore_jcol = set()
        for i in range(5, 2, -1):
            if len(ignore_jcol) >= 4:
                break
            for j in range(4):
                if j in ignore_jcol or j+1 in ignore_jcol or j+2 in ignore_jcol or j+3 in ignore_jcol:
                    if playBoard[i][j] == 0:
                        ignore_jcol.add(j)
                    if playBoard[i - 1][j + 1] == 0:
                        ignore_jcol.add(j+1)
                    if playBoard[i - 2][j + 2] == 0:
                        ignore_jcol.add(j+2) 
                    if playBoard[i - 3][j + 3] == 0:
                        ignore_jcol.add(j+3)
                    continue
                if playBoard[i][j] != player and playBoard[i][j] != 0:
                    continue
                else:
                    count = 0
                    if playBoard[i][j] == 0:
                        count += 1
                    elif playBoard[i][j] != 0:
                        continue
                    else:
                        ignore_jcol.add(j)
                    if playBoard[i - 1][j + 1] == player:
                        count += 1
                    elif playBoard[i - 1][j + 1] != 0:
                        j = j + 1
                        continue
                    else:
                        ignore_jcol.add(j + 1)
                    if playBoard[i - 2][j + 2] == player:
                        count += 1
                    elif playBoard[i - 2][j + 2] != 0:
                        j = j + 2
                        continue
                    else:
                        ignore_jcol.add(j + 2)
                    if playBoard[i - 3][j + 3] == player:
                        count += 1
                    elif playBoard[i - 3][j + 3] != 0:
                        j = j + 3
                        continue
                    else:
                        ignore_jcol.add(j + 3)
                    dict[count] += 1