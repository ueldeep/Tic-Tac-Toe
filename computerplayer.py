import time
import random
class computer_player:
    def __init__(self, player_num, mark):
        self.player_num = player_num
        self.mark = mark
    def __str__(self):
        return  'Player number:'+str(self.player_num)+', and his/her mark is:'+self.mark
    def play(self,b):
        retval = random.choice(b.get_empty_cells_keys())
        print('played:' + retval)
        time.sleep(1)
        return retval