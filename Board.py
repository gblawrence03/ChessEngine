from Piece import Piece

class Board:
    def __init__(self):
        # Set up empty board
        self.Square = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            self.Square.append(row)

    # Load a position from a FEN string.
    # TODO: 
    # - Get allowed castle moves
    # - Get active colour
    # - Get en passant target square
    def LoadFen(self, fen):
        r = 7
        f = 0
        fenBoard = fen.split(" ")[0]
        for char in fenBoard:
            if char == '/':
                f = 0
                r -= 1
            else:
                if char.isdigit():
                    f += int(char)
                else:
                    self.Square[7-r][f] = Piece.FenToPiece(char)
                    f += 1