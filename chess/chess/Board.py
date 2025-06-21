from chess.Color import WHITE, BLACK
from chess.Pawn import Pawn
from chess.Rook import Rook
from chess.King import King
from chess.Bishop import Bishop
from chess.Knight import Knight
from chess.Queen import Queen


class Board:
    def __init__(self):
        self.__board = [[None for _ in range(8)] for _ in range(8)]
        self.__player = WHITE

        self.__board[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE),
            Queen(WHITE), King(WHITE), Bishop(WHITE),
            Knight(WHITE), Rook(WHITE)
        ]
        self.__board[1] = [Pawn(WHITE) for _ in range(8)]

        self.__board[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK),
            Queen(BLACK), King(BLACK), Bishop(BLACK),
            Knight(BLACK), Rook(BLACK)
        ]
        self.__board[6] = [Pawn(BLACK) for _ in range(8)]

    @property
    def player(self) -> int:
        return self.__player

    @property
    def board(self) -> list[list]:
        return self.__board

    @staticmethod
    def validate(row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8

    def get_item(self, row: int, col: int):
        if not self.validate(row, col):
            return None
        return self.__board[row][col]

    def move_item(self, row_start: int, col_start: int, row_end: int, col_end: int):
        piece = self.get_item(row_start, col_start)
        if not piece:
            return

        self.__board[row_end][col_end] = piece
        self.__board[row_start][col_start] = None

    def change_player(self):
        self.__player = BLACK if self.player == WHITE else WHITE

    def is_check(self, color: int) -> bool:

        king_position = None

        for row in range(8):
            for col in range(8):
                piece = self.get_item(row, col)
                if piece and piece.color == color and isinstance(piece, King):
                    king_position = (row, col)
                    break
            if king_position:
                break

        if not king_position:
            raise ValueError("Король не найден на доске")

        for row in range(8):
            for col in range(8):
                piece = self.get_item(row, col)
                if piece and piece.color != color:
                    if piece.can_attack(self, row, col, *king_position):
                        return True
        return False

    def is_checkmate(self, color: int) -> bool:

        if not self.is_check(color):
            return False
        for row in range(8):
            for col in range(8):
                piece = self.get_item(row, col)
                if piece and piece.color == color:
                    for row_end in range(8):
                        for col_end in range(8):
                            if piece.can_move(self, row, col, row_end, col_end):
                                original_piece = self.get_item(row_end, col_end)

                                self.move_item(row, col, row_end, col_end)

                                if not self.is_check(color):
                                    self.move_item(row_end, col_end, row, col)
                                    if original_piece:
                                        self.__board[row_end][col_end] = original_piece
                                    return False

                                self.move_item(row_end, col_end, row, col)
                                if original_piece:
                                    self.__board[row_end][col_end] = original_piece

        return True