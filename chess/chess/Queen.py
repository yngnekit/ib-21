from chess.Color import WHITE
from chess.Figure import Figure
from chess import Board


class Queen(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wQ'
        return 'bQ'

    def can_move(self,
                 board: Board,
                 row_start: int,
                 col_start: int,
                 row_end: int,
                 col_end: int
                 ) -> bool:
        row_diff = abs(row_end - row_start)
        col_diff = abs(col_end - col_start)

        if row_diff != col_diff and row_diff != 0 and col_diff != 0:
            return False

        if row_diff == 0:
            col_step = 1 if col_end > col_start else -1
            row_step = 0
        elif col_diff == 0:
            row_step = 1 if row_end > row_start else -1
            col_step = 0
        else:
            row_step = 1 if row_end > row_start else -1
            col_step = 1 if col_end > col_start else -1

        row, col = row_start + row_step, col_start + col_step
        while row != row_end or col != col_end:
            figure = board.get_item(row, col)
            if figure:
                return False
            row += row_step
            col += col_step

        target_figure = board.get_item(row_end, col_end)
        if target_figure and target_figure.color == self.color:
            return False

        return True