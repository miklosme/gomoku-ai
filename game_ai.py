from game_gui import GomokuGameGUI, get_player_name, PLAYER_1, PLAYER_2
import numpy as np


class GomokuGameAI(GomokuGameGUI):
    def __init__(self):
        super().__init__();

    def next_move(self):
        try:
            x = np.random.randint(0, self.table_size)
            y = np.random.randint(0, self.table_size)
            return self.play_step(x, y)
        except:
            return self.next_move()

