import random
class game:
    def __init__(self, board, players):
        self.players = players
        self.board = board
    def start_game(self):
        print('Game Started!')
        print('Each player should enter his/her move in column/row notation e.g. a1, b3, etc.')
        current_player = random.randint(1,len(self.players))
        cell_key=''
        self.board.clear_board()
        while self.board.finished == False and cell_key != '-1':
            print(self.board)
            print(self.players[current_player-1])
            play = True
            while play :
                cell_key = self.players[current_player-1].play(self.board)
                if cell_key == '-1':
                    print('Game stopped by player!')
                    play = False
                else:
                    result = self.board.mark_cell(cell_key, current_player)
                    if result == 0 :
                        current_player = 1 if current_player+1 > self.board.num_players else current_player+1
                        play = False
                    elif result == 1:
                        print(self.board)
                        print(self.board.msg)
                        play = False
                    elif result == -1:
                        print(self.board.msg)
                        print('Try again!')
