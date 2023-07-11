import torch
import random
import numpy as np
from collections import deque

# from game import GomokuGame, PLAYER_1, PLAYER_2
from game_gui import GomokuGameGUI, PLAYER_1, PLAYER_2

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001


class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0.0  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = None
        self.trainer = None
        self.loss = []
        self.score = []

    def get_state(self, game):
        pass


if __name__ == "__main__":
    pass
