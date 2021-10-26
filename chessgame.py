import chessboard
import pieces

class Game():
    def startGame():

        """
        newGame = input("would you like to start a new Game? (y/n): ")
        if(newGame == 'y'):
            Game.game();
        elif( newGame == 'n'):
            print('Game Over')
        else:
            print('invalid response, please try again')
            startGame()
        """
        Game.game()
    def game():
        print('Starting new game')
        bishop = pieces.Bishop(board.board[pos[0]])
        print(bishop().pos)
        print('Opponent Biship starting: ')

Game.startGame();
