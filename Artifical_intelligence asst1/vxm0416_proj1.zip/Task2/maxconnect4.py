import sys
from MaxConnect4Game import maxConnect4Game
from calculation import Calculation
from datetime import datetime

def oneMoveGame(maxGame):
    start_time = datetime.now()
    if maxGame.pieceCount == 42:
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)
    maxGame.aiPlay()
    print ('Game after move:')
    maxGame.printPlayBoard()
    maxGame.player1Score = maxGame.calculation.getScore(maxGame.playBoard, 1)
    maxGame.player2Score = maxGame.calculation.getScore(maxGame.playBoard, 2)
    print('Score: Player 1 = %d, Player 2 = %d\n' % (maxGame.player1Score, maxGame.player2Score))
    maxGame.printPlayBoardToFile()
    maxGame.gameFile.close()
    print("Start Time : %s" % (start_time.strftime('%H:%M:%s')))
    print("Finish Time : %s" % (datetime.now().strftime('%H:%M:%s')))
    print("Time difference : %s" % (datetime.now() - start_time))

def interactiveGame(maxGame):
    if maxGame.pieceCount == 42:
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)
    maxGame.depth = int(sys.argv[4])
    computer_txt = open("computer.txt", "w")
    human_txt = open("human.txt", "w")
    if sys.argv[3] == "computer-next":
        while (True):
            maxGame.presentTurn = 1
            maxGame.aiPlay()
            print ('Game after computer move:')
            maxGame.printPlayBoard()
            maxGame.writePlayBoardToFile(computer_txt, 1)
            maxGame.player1Score = maxGame.calculation.getScore(maxGame.playBoard, 1)
            maxGame.player2Score = maxGame.calculation.getScore(maxGame.playBoard, 2)
            print('Score: Player 1 = %d, Player 2 = %d\n' % (maxGame.player1Score, maxGame.player2Score))
            while maxGame.pieceCount != 42:
                game_col = input("Enter column number from 1 to 7 or q to quit: ")
                if game_col != "q":
                    maxGame.presentTurn = 2
                    if not 0 < int(game_col) < 8:
                        print("Column not valid, Enter column number.")
                        continue
                    if maxGame.playPiece(int(game_col)-1):
                        print ('Game after human  move:')
                        maxGame.printPlayBoard()
                        maxGame.writePlayBoardToFile(human_txt, 2)
                        maxGame.player1Score = maxGame.calculation.getScore(maxGame.playBoard, 1)
                        maxGame.player2Score = maxGame.calculation.getScore(maxGame.playBoard, 2)
                        print('Score: Player 1 = %d, Player 2 = %d\n' % (maxGame.player1Score, maxGame.player2Score))
                        break
                    if not maxGame.playPiece(int(game_col) - 1):
                        print("Column number: %d is full. Try other column." % game_col)
                        continue
                else:
                    exit()
            if maxGame.pieceCount == 42:
                if maxGame.player1Score > maxGame.player2Score:
                    print("Player 1 won the Game !")
                if maxGame.player1Score == maxGame.player2Score:
                    print("The game is a Tie !")
                if maxGame.player1Score < maxGame.player2Score:
                    print("Player 2 won the Game !")
                print("Game Over")
                exit()
    elif sys.argv[3] == "human-next":
        while (True):
            while maxGame.pieceCount != 42:
                game_col = input("Enter column number from 1 to 7 or q to quit: ")
                if game_col != "q":
                    maxGame.presentTurn = 1
                    if maxGame.playPiece(int(game_col)-1):
                        print ('Game after human move:')
                        maxGame.printPlayBoard()
                        maxGame.writePlayBoardToFile(human_txt, 1)
                        maxGame.player1Score = maxGame.calculation.getScore(maxGame.playBoard, 1)
                        maxGame.player2Score = maxGame.calculation.getScore(maxGame.playBoard, 2)
                        print('Score: Player 1 = %d, Player 2 = %d\n' % (maxGame.player1Score, maxGame.player2Score))
                        break
                else:
                    exit()
            if maxGame.pieceCount == 42:
                exit()
            maxGame.presentTurn = 2
            maxGame.aiPlay()
            print ('Game after computer move:')
            maxGame.printPlayBoard()
            maxGame.writePlayBoardToFile(computer_txt, 2)
            maxGame.player1Score = maxGame.calculation.getScore(maxGame.playBoard, 1)
            maxGame.player2Score = maxGame.calculation.getScore(maxGame.playBoard, 2)
            print('Score: Player 1 = %d, Player 2 = %d\n' % (maxGame.player1Score, maxGame.player2Score))
    computer_txt.close()
    human_txt.close()

def main(argv):
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)
    game_mode, inFile = argv[1:3]
    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)
    maxGame = maxConnect4Game(Calculation())
    try:
        maxGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")
    file_lines = maxGame.gameFile.readlines()
    if file_lines:
        maxGame.playBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
        maxGame.presentTurn = int(file_lines[-1][0])
    else:
        maxGame.playBoard = [[0 for _ in range(7)] for _ in range(6)]
        maxGame.presentTurn = 1
    maxGame.gameFile.close()
    print ('\nMaxConnect-4 game\n')
    print ('Game  before move:')
    maxGame.printPlayBoard()
    maxGame.checkPieceCount()
    maxGame.player1Score = maxGame.calculation.getScore(maxGame.playBoard, 1)
    maxGame.player2Score = maxGame.calculation.getScore(maxGame.playBoard, 2)
    print('Score: Player 1 = %d, Player 2 = %d\n' % (maxGame.player1Score, maxGame.player2Score))
    if game_mode == 'interactive':
        interactiveGame(maxGame)
    else:
        game_mode == 'one-move'
        outFile = argv[3]
        try:
            maxGame.gameFile = open(outFile, 'w')
            maxGame.depth = int(argv[4])
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(maxGame)

if __name__ == '__main__':
    main(sys.argv)



