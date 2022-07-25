class TicTacToe:

    def __init__(self):
        self.board = self.__setBoard()
        self.moves = self.__setMoves()
        self.winner = None
        self.turn = True
        self.p1Moves = set()
        self.p2Moves = set()

    # define our clear function
    def clear(self):
        from os import system, name
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    # end of clear

    def __setMoves(self):
        return {str(row) + str(col) for row in self.board.keys() for col in range(len(self.board[row]))}
    # end of __setMoves()

    def __setBoard(self):
        temp = {
            'A' : ['_', '_', '_'],
            'B' : ['_', '_', '_'],
            'C' : ['_', '_', '_']
        }

        return temp
    # end of setBoard

    def validate(self, player):

        wins = [
            {'A0','A1','A2'}, {'B0','B1','B2'}, {'C0','C1','C2'},
            {'A0','B0','C0'}, {'A1','B1','C1'}, {'A2','B2','C2'},
            {'A0','B1','C2'}, {'A2','B1','C0'}
        ]
        for combo in wins:
            if len(combo - player) == 0:
                return True
        # no win found
        return False
    # end validate

    def __placeToken(self, token, row, col):
        self.board[row][col] = token
    # end of .__placeToken()

    def play(self):
        move = ''
        token = ''

        print('Possible Moveset:', sorted(list(self.moves)))
        if self.turn:
            self.turn = False
            token = '0'
            print('Player 1, please input a valid move.')
        else:
            self.turn = True
            token = 'X'
            print('Player 2, please input a valid move.')

        while not move or move not in self.moves:
            move = input(' -- Enter token location: ').upper()
            if move not in self.moves:
                print(' -- Invalid input ...')
        else:
            print('Your location choice:', move)
            self.moves.remove(move)
            self.__placeToken(token, move[0], int(move[1]))
            if self.turn:
                self.p2Moves.add(move)
            else:
                self.p1Moves.add(move)
    # end of play()


    def __str__(self):
        output = '     Tic Tac Toe\n ' + '-'*19 + '\n'
        output += '| '+' '*6 + '0' + ' '*3 + '1' + ' '*3 + '2' + '   | P1: 0, P2: X\n'

        for key, value in self.board.items():
            output += f'| {key} : [ {value[0]} | {value[1]} | {value[2]} ] |\n'
        output += '|'+'_'*19+'|\n'

        return output
    # end of str()
# end of TicTacToe()

start = input('Start game?')
while start in ('Yes','yes'):
    x = TicTacToe()
    print(x)


    for i in range(9):
        x.play()
        print(x)
        x.validate(x.p1Moves)
        if x.validate(x.p1Moves) == True:
            print('Player 1 is the winner')
            break
        x.validate(x.p2Moves)
        if x.validate(x.p2Moves) == True:
            print('Player 2 is the winner')
            break

    again = input('Play again?')
    if again in ('Yes','yes'):
        x.__setBoard
        x.__setMoves
        continue
    else:
        print('GG WP')
        x.clear
        break