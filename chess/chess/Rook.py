from chess.Color import WHITE
from chess.Figure import Figure
from chess import Board


class Rook(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wR'
        return 'bR'

    def can_move(self,
                 board: Board,
                 row_start: int,
                 col_start: int,
                 row_end: int,
                 col_end: int
                 ) -> bool:

        if row_start != row_end and col_start != col_end:
            return False

        row_step = 1 if row_end > row_start else -1 if row_end < row_start else 0
        col_step = 1 if col_end > col_start else -1 if col_end < col_start else 0

        if row_start != row_end:
            for row in range(row_start + row_step, row_end, row_step):
                figure = board.get_item(row, col_start)
                if figure:
                    return False

        elif col_start != col_end:
            for col in range(col_start + col_step, col_end, col_step):
                figure = board.get_item(row_start, col)
                if figure:
                    return False

        return True