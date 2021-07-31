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
            ['--','--','--','--','--','--','--','--']
        ]
        self.white_move = True
        self.moveLog = []
        self.list_abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
        self.list_123 = ['1','2','3','4','5','6','7','8']
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        
    def choosePosition(self, arg):
        try:
            for char in self.list_abc:
                if arg[0] == char:
                    for num in self.list_123:
                        if arg[1] == num:
                            char_position = self.list_abc.index(arg[0])
                            num_position = self.list_123.index(arg[1])
                            self.board[num_position][char_position] = "wN"
                            print(f"./cavalo {arg}")
        except:
            print("Um erro ocorreu")

class Move():
    ranksToRows = {"1": 7, "2": 6,"3": 5, "4": 4,
                    "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                     'f': 5, 'g': 6, 'h': 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, start_Sq, end_Sq, board):
        self.startRow = start_Sq[0]
        self.startCol = start_Sq[1]
        self.endRow = end_Sq[0]
        self.endCol = end_Sq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
    
    def getChessNotation(self):
        return self.getRankFile(self.endRow, self.endCol)
    
    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]