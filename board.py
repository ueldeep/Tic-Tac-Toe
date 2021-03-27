import string 
import random
class board:
    def __init__(self, size=3, num_players=2, marks=('x','o')):
        if size<3 or size > 10:
            raise Exception('Error: Borad  size should be between 3 and 10')
        elif len(marks)!=num_players:
            raise Exception('Error: Number of players and number of marks doesn''t match')
        else:    
            self.finished = False
            self.winner = 0
            self.msg = ''
            self.size=size
            self.empity_cells = size * size
            self.num_players=num_players
            self.marks=marks
            self.cells = dict()
            self.diagonals = [[],[]]
            self.columns = string.ascii_lowercase[:size]
            for col in self.columns:
                for row in range(1,size+1):
                    key = col+str(row)
                    self.cells[key] = ' '
                    if self.columns.index(col)+1 == row:
                        self.diagonals[0].append(key)
                    if self.columns[::-1].index(col)+1 == row:
                        self.diagonals[1].append(key)
            
            self.players = [ dict({'Num':i+1, 'Mark':marks[i]}) for i in range(self.num_players)]
            for player in self.players:
                for col in self.columns:
                    player[str(col)] = 0
                for row in range(1,size+1):
                    player[str(row)] = 0
                for diag in self.diagonals:
                    player[''.join(diag)] = 0
    
    def __str__(self):
        columns = '    '+'   '.join(self.columns)+u'\n'
        topline = (u'  '+ u'\u250C'+u'\u2500'*3)+(u'\u252c'+u'\u2500'*3)*(self.size-1)+(u'\u2510')+u'\n'
        dataline = (u' '+ u'\u2502'+u' '+u'x'+u' ')+(u'\u2502'+u' '+u'o'+u' ')*(self.size-1)+(u'\u2502')+u'\n'
        inbetweenline = (u'  '+u'\u251C'+u'\u2500'*3)+(u'\u253c'+u'\u2500'*3)*(self.size-1)+(u'\u2524')+u'\n'
        bottomline = (u'  '+u'\u2514'+u'\u2500'*3)+(u'\u2534'+u'\u2500'*3)*(self.size-1)+(u'\u2518')+u'\n'
        board = columns
        for row in range(1,self.size+1):
            dataline = str(row) + u' '+ u'\u2502'
            for data in self.get_cells_values(row):
                dataline += u' '+data+ u' '+u'\u2502'
            else:
                dataline += u'\n'
            if row == 1 :
                board += topline + dataline
            else:
                board += inbetweenline + dataline
        else:
            board +=bottomline
        return board

    def get_cells_values(self,key):
        retval = list()
        for cell_key in self.cells.keys():
            if str(key) in cell_key:
                retval.append(self.cells[cell_key])
        return retval
   

    def mark_cell(self, cell_key, player_num):
        retval = 0
        cell_value = self.cells.get(cell_key,-1)
        if self.finished:
            retval = 1
            self.msg =  'Error: Game finished!'
        elif cell_value == -1:
            retval = -1
            self.msg =  'Error: Wrong cell reference!'
        elif cell_value !=' ':
            retval = -1
            self.msg =  'Error: Cell is not empty!'
        else:
            self.cells[cell_key] = self.players[player_num-1]['Mark']
            self.empity_cells -= 1
            for key in self.get_cell_locations(cell_key):
                self.players[player_num-1][key]+=1
                
            for value in self.players[player_num-1].values():
                if value == self.size:
                    retval = 1
                    self.finished = True
                    self.msg = 'Game Over! winner is player number: '+str(player_num)
            if retval == 0 and self.empity_cells == 0:
                retval = 1
                self.finished = True
                self.msg = 'Game Over! No winner!'
        return retval

    def get_cell_locations(self,cell_key):
        locations = list()
        locations.append(cell_key[0])
        locations.append(cell_key[1])
        for i in range(len(self.diagonals)):
                for j in range(len(self.diagonals[i])):
                    if self.diagonals[i][j] == cell_key:
                        locations.append(''.join(self.diagonals[i]))
                        
        return locations
    def get_marked_cells_keys(self, mark):
        retval = list()
        for key in self.cells:
            if self.cells[key] == mark:
                retval.append(key)
        return retval

    def get_empty_cells_keys(self):
        return self.get_marked_cells_keys(' ')
    
    def clear_board(self):
        self.finished = False
        self.winner = 0
        self.empity_cells = self.size * self.size
        for key in self.cells:
            self.cells[key] = ' '
        for player in self.players:
            for col in self.columns:
                player[str(col)] = 0
            for row in range(1,self.size+1):
                player[str(row)] = 0
            for diag in self.diagonals:
                player[''.join(diag)] =0
