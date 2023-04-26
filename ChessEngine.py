import pygame as pg
from BoardRenderer import BoardRenderer
from Piece import Piece
from Board import Board
import threading 
import time
import sys

board = Board()

pg.init()
window = pg.display.set_mode((800, 600))
renderer = BoardRenderer(window, board, (181, 136, 99), (240, 217, 181))

# Get position from FEN if one was given, otherwise starting position
if len(sys.argv) == 1:
    board.LoadFen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
else:
    board.LoadFen(sys.argv[1])

# This thread will later be used to process moves
def process():
    turn = 0 # 0 means white's turn, 1 means black's turn
    return

process_thread = threading.Thread(target=process)
process_thread.start()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            process_thread.join()
            exit()
    renderer.DrawBoard()
    pg.display.update()