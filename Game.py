import random
import numpy as np

class Game:
    def __init__ (self, game):
        self.game = game
        
    def stack(self):
        new_grid = np.zeros((4,4))
        for i in range(4):
            position = 0
            
            for j in range(4):
                if self.game[i][j] != 0:
                    new_grid[i][position] = self.game[i][j]
                    position += 1
                    
        self.game = new_grid
        
    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.game[i][j] != 0 and self.game[i][j] == self.game[i][j+1]:
                    self.game[i][j] *= 2
                    self.game[i][j+1] = 0
                    self.score += self.game[i][j]
                    
    def add_new_tile(self):
        i = random.randint(0,3)
        j = random.randint(0,3)
        while(self.game[i][j] != 0):
            i = random.randint(0,3)
            j = random.randint(0,3)
        self.game[i][j] = random.choice([2,4])
        
    def move_left(self):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        
    def move_right(self):
        self.game = np.flip(self.game, 1)
        self.stack()
        self.combine()
        self.stack()
        self.game = np.flip(self.game, 1)
        self.add_new_tile()
        
    def move_up(self):
        self.game = self.game.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.game = self.game.transpose()
        self.add_new_tile()
        
    def move_down(self):
        self.game = self.game.transpose()
        self.game = np.flip(self.game, 1)
        self.stack()
        self.combine()
        self.stack()
        self.game = np.flip(self.game, 1)
        self.game = self.game.transpose()
        self.add_new_tile()
        