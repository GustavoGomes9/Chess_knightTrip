
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
        self.list_abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
        self.list_123 = ['1','2','3','4','5','6','7','8']
    
    def choosePosition(self, arg):
        for char in self.list_abc:
            if arg[0] == char:
                for num in self.list_123:
                    if arg[1] == num:
                        char_position = self.list_abc.index(arg[0])
                        num_position = self.list_123.index(arg[1])
                        self.board[num_position][char_position] = "wN"
                        print(self.board)

p = input("casa :     ")
gs = GameState()
gs.choosePosition(p)