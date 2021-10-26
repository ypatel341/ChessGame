import chessboard

def update_updown(board):

def update_diag(board):

class Rook():
    def __init__(self, pos):
        self.name = "R"
        self.color = "black"
        self.pos = chessboard.ChessBoard.Board[2][5];
        """
        self.pos = newBoard['C'][5]
        """
    def valid_moves(self, board, start, to):
        if start[0] == to[0] or start[1] == to[1]:
            return update_updown(board, start, to)

class Bishop():
    def __init__(self, pos):
        self.name = "B"
        self.color = "white"
        """
        self.pos = newBoard['F'][3]
        """
    def valid_moves(self, board, start, to):
        if start[0] == to[0] or start[1] == to[1]:
            return update_diag(board, start, to)
