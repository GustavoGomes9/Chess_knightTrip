"""Responsavél pela a construção inical do trabuleiro"""

class GameState():
    def __init__(self):
        self.board = [
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--',"--"]
        ]
        self.white_move = True
        self.move_log = []
    
    def choosePosition(self, arg):
        if arg == "c1":
            self.board[0][2] = "wN"
            print(self.board)
            