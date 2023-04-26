import pygame as pg
from Piece import Piece
import io

class BoardRenderer:
    def __init__(self, window, board, dark_colour, light_colour):
        self.DarkColour = dark_colour
        self.LightColour = light_colour
        self.Window = window
        self.Board = board
        self.BoardSize = min(window.get_height(), window.get_width())
        self.SquareSize = self.BoardSize / 8

        self.LoadTextures()
        self.ResizeTextures()

    def DrawBoard(self):
        for f in range(0, 8):
            for r in range(0, 8):
                self.DrawSquare(f, r, self.Board.Square[r][f])

    # Draws a single square by deciding whether it is light or dark 
    # and then adding the piece if there is one
    def DrawSquare(self, f, r, piece):
        if ((f + r) % 2) == 1:
            colour = self.DarkColour
        else: 
            colour = self.LightColour
        square_x = self.SquareSize * f
        square_y = self.SquareSize * r
        pg.draw.rect(self.Window, colour, pg.Rect(square_x, square_y, self.SquareSize, self.SquareSize))
        if piece != None:
            self.Window.blit(self.Textures[piece], (square_x, square_y))

    # Load the piece textures from files
    def LoadTextures(self):
        self.Textures = dict()
        self.Textures[Piece.Black | Piece.Pawn] = pg.image.load('./Assets/bP.svg')
        self.Textures[Piece.Black | Piece.Knight] = pg.image.load('./Assets/bN.svg')
        self.Textures[Piece.Black | Piece.Bishop] = pg.image.load('./Assets/bB.svg')
        self.Textures[Piece.Black | Piece.Rook] = pg.image.load('./Assets/bR.svg')
        self.Textures[Piece.Black | Piece.Queen] = pg.image.load('./Assets/bQ.svg')
        self.Textures[Piece.Black | Piece.King] = pg.image.load('./Assets/bK.svg')
        self.Textures[Piece.White | Piece.Pawn] = pg.image.load('./Assets/wP.svg')
        self.Textures[Piece.White | Piece.Knight] = pg.image.load('./Assets/wN.svg')
        self.Textures[Piece.White | Piece.Bishop] = pg.image.load('./Assets/wB.svg')
        self.Textures[Piece.White | Piece.Rook] = pg.image.load('./Assets/wR.svg')
        self.Textures[Piece.White | Piece.Queen] = pg.image.load('./Assets/wQ.svg')
        self.Textures[Piece.White | Piece.King] = pg.image.load('./Assets/wK.svg')

    # Resize textures to square size
    def ResizeTextures(self):
        for t in self.Textures.keys():
            self.Textures[t] = pg.transform.scale(self.Textures[t], (self.SquareSize, self.SquareSize))