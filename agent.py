import torch
import random
import numpy as np
from collections import deque
import pygame

# from game import GomokuGame, PLAYER_1, PLAYER_2
from game_ai import GomokuGameAI, PLAYER_1, PLAYER_2, get_player_name

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001


class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0.0  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # popleft()
        # self.model = Linear_QNet(11, 256, 3)
        # self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)
        self.model = None
        self.trainer = None
        self.loss = []
        self.score = []

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    def get_action(self, state):
        pass


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = GomokuGameAI()

    game.reset(table_size=6, max_pieces=30, min_pieces_to_win=4)
    game._draw()

    while True:
        for event in pygame.event.get():
            pass

        game_over, winner = game.next_move()
        pygame.time.wait(1000)

        game._draw()

        if game_over == True:
            print(
                "Result:",
                "Draw" if winner == None else get_player_name(winner) + " wins",
            )
            break

    game.exit()

    # while True:
    #     # get old state
    #     state_old = agent.get_state(game)

    #     # get move
    #     final_move = agent.get_action(state_old)

    #     # perform move and get new state
    #     reward, done, score = game.play_step(final_move)
    #     state_new = agent.get_state(game)

    #     # train short memory
    #     agent.train_short_memory(state_old, final_move, reward, state_new, done)

    #     # remember
    #     agent.remember(state_old, final_move, reward, state_new, done)

    #     if done:
    #         # train long memory, plot result
    #         game.reset()
    #         agent.n_games += 1
    #         agent.train_long_memory()

    #         if score > record:
    #             record = score
    #             agent.model.save()

    #         print("Game", agent.n_games, "Score", score, "Record", record)

    #         plot_scores.append(score)
    #         total_score += score
    #         mean_score = total_score / agent.n_games
    #         plot_mean_scores.append(mean_score)
    #         plot(plot_scores, plot_mean_scores)


if __name__ == "__main__":
    train()
