import time
import random
class computer_player:
    def __init__(self, player_num, mark):
        self.player_num = player_num
        self.mark = mark
    def __str__(self):
        return  'Player number:'+str(self.player_num)+', and his/her mark is:'+self.mark

    def play(self,b):
        choices = dict()
        retval = ''
        higher_value=0
        for empity_cell in b.get_empty_cells_keys():
            choices[empity_cell] = self.evaluate_play(b,empity_cell)
            if choices[empity_cell] > higher_value:
                higher_value = choices[empity_cell]
                retval = empity_cell
                if higher_value == 100:
                    break
        if retval == '': retval = random.choice(b.get_empty_cells_keys())
        print('played:' + retval)
        time.sleep(1)
        return retval
    
    def evaluate_play(self,b, cell_key):
        cell_locations = b.get_cell_locations(cell_key)
        evaluation = 0
        for player in b.players:
            #print (f'cell {cell_key}, '+'player: ' + str(player['Num']))
            myself = True if player['Num'] == self.player_num else False
            higher_value =0
            for location in cell_locations:
                if (player[location] > higher_value) : higher_value = player[location] 
             
            if (higher_value + 1) == b.size:
                if myself:
                    evaluation = 100
                    break
                else:
                    evaluation = 50
            else:
                if myself:
                    if(higher_value * 2 > evaluation): evaluation =  (higher_value * 2)
                else:
                    if higher_value > evaluation : evaluation =  higher_value
        return evaluation              