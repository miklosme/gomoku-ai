from game_gui import GomokuGameGUI, get_player_name, PLAYER_1, PLAYER_2
import numpy as np


class GomokuTest(GomokuGameGUI):
    def __init__(self):
        super().__init__()


def debug_state(game):
    other_player = PLAYER_1 if game.current_player == PLAYER_2 else PLAYER_2

    current_player_pieces = np.where(game.table == game.current_player, 1, 0)
    other_player_pieces = np.where(game.table == other_player, 1, 0)

    map = current_player_pieces - other_player_pieces
    flat = np.array(map, dtype=int).flatten()

    print(flat)


if __name__ == "__main__":
    game = GomokuTest()

    game.reset(table_size=6, max_pieces=30, min_pieces_to_win=4)

    game._draw()

    while True:
        game_over, winner = game.loop(on_change=debug_state)

        if game_over == True:
            print(
                "Result:",
                "Draw" if winner == None else get_player_name(winner) + " wins",
            )
            break

    game.exit()
