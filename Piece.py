# Internal representation of a piece. 
# Requires 4 bits - first bit represents colour, last three represent the piece

class Piece:
    Empty = 0
    King = 1
    Pawn = 2
    Knight = 3
    Bishop = 4
    Rook = 5
    Queen = 6

    White = 8
    Black = 0

    def FenToPiece(fen):
        if fen.isupper():
            colour = Piece.White
        else:
            colour = Piece.Black
        return colour | Piece.CharToPiece[fen.lower()]
        
    CharToPiece = {'k': King, 'p': Pawn, 'n': Knight, 'b': Bishop, 'r': Rook, 'q': Queen}