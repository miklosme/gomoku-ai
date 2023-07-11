import pygame
from game import GomokuGame, PLAYER_1, PLAYER_2


def get_player_name(player):
    if player == PLAYER_1:
        return "White"
    elif player == PLAYER_2:
        return "Black"
    else:
        raise Exception("Invalid player")


BACKGROUND = (150, 150, 150)
PLAYER_1_COLOR = (255, 255, 255)
PLAYER_2_COLOR = (0, 0, 0)
TABLE_LINES = (190, 190, 190)

BLOCK_SIZE = 20
TABLE_MARGIN = 50

pygame.init()
font = pygame.font.SysFont("arial", 25)


class GomokuGameGUI(GomokuGame):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Gomoku")

    def _draw(self):
        self.display.fill(BACKGROUND)

        for i in range(self.table_size + 1):
            pygame.draw.line(
                self.display,
                TABLE_LINES,
                (TABLE_MARGIN, TABLE_MARGIN + i * BLOCK_SIZE),
                (
                    TABLE_MARGIN + self.table_size * BLOCK_SIZE,
                    TABLE_MARGIN + i * BLOCK_SIZE,
                ),
            )
            pygame.draw.line(
                self.display,
                TABLE_LINES,
                (TABLE_MARGIN + i * BLOCK_SIZE, TABLE_MARGIN),
                (
                    TABLE_MARGIN + i * BLOCK_SIZE,
                    TABLE_MARGIN + self.table_size * BLOCK_SIZE,
                ),
            )

        for i in range(self.table_size):
            for j in range(self.table_size):
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

    def loop(self, on_change=None):
        x = None
        y = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                x = (x - TABLE_MARGIN) // BLOCK_SIZE
                y = (y - TABLE_MARGIN) // BLOCK_SIZE

        if x == None or y == None:
            return False, None

        try:
            game_over, winner = super().play_step(x, y)
        except:
            print("Invalid move")
            return False, None

        self._draw()

        if on_change != None:
            on_change(self)

        return game_over, winner

    def exit(self):
        pygame.quit()


if __name__ == "__main__":
    game = GomokuGameGUI()

    game._draw()

    while True:
        game_over, winner = game.loop()

        if game_over == True:
            print(
                "Result:",
                "Draw" if winner == None else get_player_name(winner) + " wins",
            )
            break

    game.exit()
