from chess.Color import WHITE
from chess.Figure import Figure
from chess import Board


class Bishop(Figure):
    @property
    def char(self) -> str:
        if self.color == WHITE:
            return 'wB'
        return 'bB'

    def can_move(
        self,
        board: Board,
        row_start: int,
        col_start: int,
        row_end: int,
        col_end: int
    ) -> bool:

        if abs(row_end - row_start) != abs(col_end - col_start):
            return False

        row_step = 1 if row_end > row_start else -1
        col_step = 1 if col_end > col_start else -1

        row, col = row_start + row_step, col_start + col_step

        while row != row_end and col != col_end:
            if board.get_item(row, col):
                return False
            row += row_step
            col += col_step

        target_piece = board.get_item(row_end, col_end)
        if target_piece and target_piece.color == self.color:
            return False

        return True


