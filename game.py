from collections import namedtuple
import numpy as np

TABLE_SIZE = 19
MAX_PIECES = 200
MIN_PIECES_TO_WIN = 5

PLAYER_1 = 1
PLAYER_2 = 2

DIRECTIONS = [
    (0, 1),  # right
    (1, 0),  # down
    (1, 1),  # down right
    (1, -1),  # down left
]


class GomokuGame:
    def __init__(self):
        self.reset()

    def reset(
        self,
        table_size=TABLE_SIZE,
        max_pieces=MAX_PIECES,
        min_pieces_to_win=MIN_PIECES_TO_WIN,
    ):
        self.table_size = table_size
        self.max_pieces = max_pieces
        self.min_pieces_to_win = min_pieces_to_win
        self.pieces_used = 0
        self.table = np.zeros((self.table_size, self.table_size))
        self.current_player = PLAYER_1
        self.game_over = False
        self.winner = None

    def play_step(self, x, y):
        current_player = self.current_player

        try:
            if x < 0 or y < 0:
                raise Exception("Invalid position")

            if self.table[y][x] == 0:
                self.table[y][x] = current_player
            else:
                raise Exception("Invalid position")
        except:
            raise Exception("Invalid position")

        self.pieces_used += 1
        self.current_player = PLAYER_1 if current_player == PLAYER_2 else PLAYER_2

        return self._check_win(x, y, current_player)

    def _check_win(self, current_x, current_y, player):
        # check win
        # iterates self.min_pieces_to_win times in each direction and their opposite
        max_connected = 0
        for dir in DIRECTIONS:
            connected = 1
            position = (current_y, current_x)
            for i in range(self.min_pieces_to_win):
                position = (position[0] + dir[0], position[1] + dir[1])
                if (
                    position[0] < 0
                    or position[1] < 0
                    or position[0] >= self.table_size
                    or position[1] >= self.table_size
                ):
                    break

                if self.table[position[0]][position[1]] == player:
                    connected += 1
                else:
                    break

            # check opposite direction
            position = (current_y, current_x)

            for i in range(self.min_pieces_to_win):
                position = (position[0] - dir[0], position[1] - dir[1])
                if (
                    position[0] < 0
                    or position[1] < 0
                    or position[0] >= self.table_size
                    or position[1] >= self.table_size
                ):
                    break

                if self.table[position[0]][position[1]] == player:
                    connected += 1
                else:
                    break

            if connected > max_connected:
                max_connected = connected

        if max_connected >= self.min_pieces_to_win:
            self.game_over = True
            self.winner = player
            return self.game_over, self.winner

        # check draw
        if self.pieces_used == self.max_pieces:
            self.game_over = True
            self.winner = None
            return self.game_over, self.winner

        return self.game_over, self.winner
