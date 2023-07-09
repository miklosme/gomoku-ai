import pygame
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.SysFont("arial", 25)

BACKGROUND = (150, 150, 150)
PLAYER_1_COLOR = (255, 255, 255)
PLAYER_2_COLOR = (0, 0, 0)
TABLE_LINES = (190, 190, 190)

BLOCK_SIZE = 20
TABLE_SIZE = 19
TABLE_MARGIN = 50
MAX_PIECES = 200
MIN_PIECES_TO_WIN = 5

PLAYER_1 = 1
PLAYER_2 = 2

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1),
]


def get_player_name(player):
    if player == PLAYER_1:
        return "White"
    elif player == PLAYER_2:
        return "Black"
    else:
        raise Exception("Invalid player")


class GomokuGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Gomoku")

        self.reset()

    def reset(self):
        self.pieces_used = 0
        self.table = np.zeros((TABLE_SIZE, TABLE_SIZE))
        self.current_player = PLAYER_1
        self.game_over = False
        self.winner = None

    def draw(self):
        self.display.fill(BACKGROUND)

        for i in range(TABLE_SIZE + 1):
            pygame.draw.line(
                self.display,
                TABLE_LINES,
                (TABLE_MARGIN, TABLE_MARGIN + i * BLOCK_SIZE),
                (
                    TABLE_MARGIN + (TABLE_SIZE) * BLOCK_SIZE,
                    TABLE_MARGIN + i * BLOCK_SIZE,
                ),
            )
            pygame.draw.line(
                self.display,
                TABLE_LINES,
                (TABLE_MARGIN + i * BLOCK_SIZE, TABLE_MARGIN),
                (
                    TABLE_MARGIN + i * BLOCK_SIZE,
                    TABLE_MARGIN + (TABLE_SIZE) * BLOCK_SIZE,
                ),
            )

        for i in range(TABLE_SIZE):
            for j in range(TABLE_SIZE):
                if self.table[i][j] == PLAYER_1:
                    pygame.draw.rect(
                        self.display,
                        PLAYER_1_COLOR,
                        pygame.Rect(
                            TABLE_MARGIN + j * BLOCK_SIZE,
                            TABLE_MARGIN + i * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE,
                        ),
                    )
                elif self.table[i][j] == PLAYER_2:
                    pygame.draw.rect(
                        self.display,
                        PLAYER_2_COLOR,
                        pygame.Rect(
                            TABLE_MARGIN + j * BLOCK_SIZE,
                            TABLE_MARGIN + i * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE,
                        ),
                    )

        text = font.render(
            "Current player: "
            + get_player_name(self.current_player)
            + " | Pieces used: "
            + str(self.pieces_used),
            True,
            (0, 0, 0),
        )
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def play_step(self):
        x = None
        y = None
        current_player = self.current_player

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # mouse click
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                x = (x - TABLE_MARGIN) // BLOCK_SIZE
                y = (y - TABLE_MARGIN) // BLOCK_SIZE

                try:
                    if x < 0 or y < 0:
                        continue

                    if self.table[y][x] == 0:
                        self.table[y][x] = self.current_player
                        self.pieces_used += 1
                        self.current_player = (
                            PLAYER_1 if self.current_player == PLAYER_2 else PLAYER_2
                        )
                except:
                    pass

        self.draw()

        if x == None or y == None:
            return False, None

        # check win
        # iterates MIN_PIECES_TO_WIN times in each direction and their opposite
        max_connected = 0
        for dir in DIRECTIONS:
            connected = 1
            position = (y, x)
            for i in range(MIN_PIECES_TO_WIN):
                position = (position[0] + dir[0], position[1] + dir[1])
                if (
                    position[0] < 0
                    or position[1] < 0
                    or position[0] >= TABLE_SIZE
                    or position[1] >= TABLE_SIZE
                ):
                    break

                if self.table[position[0]][position[1]] == current_player:
                    connected += 1
                else:
                    break

            position = (y, x)

            for i in range(MIN_PIECES_TO_WIN):
                position = (position[0] - dir[0], position[1] - dir[1])
                if (
                    position[0] < 0
                    or position[1] < 0
                    or position[0] >= TABLE_SIZE
                    or position[1] >= TABLE_SIZE
                ):
                    break

                if self.table[position[0]][position[1]] == current_player:
                    connected += 1
                else:
                    break

            if connected > max_connected:
                max_connected = connected

        if max_connected >= MIN_PIECES_TO_WIN:
            self.game_over = True
            self.winner = current_player
            return self.game_over, self.winner

        # check draw
        if self.pieces_used == MAX_PIECES:
            self.game_over = True
            self.winner = None
            return self.game_over, self.winner

        return False, None


if __name__ == "__main__":
    game = GomokuGame()

    game.draw()

    while True:
        game_over, winner = game.play_step()

        if game_over == True:
            break

    print("Result:", "Draw" if winner == None else get_player_name(winner) + " wins")

    pygame.quit()
