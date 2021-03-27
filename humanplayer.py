class human_player:
    def __init__(self, player_num, mark):
        self.player_num = player_num
        self.mark = mark
    def __str__(self):
        return  'Player number:'+str(self.player_num)+', and his/her mark is:'+self.mark
    def play(self,b=None):
        return str(input('Enter your play:'))