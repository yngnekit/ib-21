import re
from chess import Board
from chess.Color import WHITE


def convert(point: str) -> tuple[int, int]:
    if len(point) != 2:
        raise ValueError("Неверный формат координат")
    char, num = point[0], point[1]
    if not ('A' <= char.upper() <= 'H') or not ('1' <= num <= '8'):
        raise ValueError("Координаты выходят за пределы доски")
    row = int(num) - 1
    col = ord(char.upper()) - ord('A')
    return row, col


def print_board(_board: Board) -> None:
    for y in range(8, 0, -1):
        print('  +' + '----+' * 8)
        print(f'{y} |', end='')
        for x in range(8):
            item = _board.get_item(y - 1, x)
            print(' ', end='')
            if not item:
                print('  ', end='')
            else:
                print(item.char, end='')
            print(' |', end='')
        print()
    print('  +' + '----+' * 8)
    print('  ', end='')
    for x in range(8):
        c = chr(ord('A') + x)
        print(f'   {c} ', end='')
    print()
    print('Команды:')
    print('    exit                - выход')
    print('    move <from> <to>    - ход из клетки <from> в клетку <to>')
    print()
    if _board.player == WHITE:
        print('Ход белых')
    else:
        print('Ход черных')

board = Board()

while True:
    print_board(board)

    if board.is_check(board.player):
        print("ШАХ!")
        if board.is_checkmate(board.player):
            print("МАТ! Игра окончена.")
            break

    try:
        cmd = input('Команда: ').strip()
        if cmd.lower() == 'exit':
            break
        if not cmd.lower().startswith('move'):
            raise Exception(f'Неизвестная команда: {cmd}')
        cmd = cmd.replace('move', '').strip().upper()
        parts = cmd.split()
        if len(parts) != 2:
            raise Exception('Неверный формат ввода!')

        start, end = map(convert, parts)
        if start == end:
            raise Exception('Мы топчимся на месте')

        piece = board.get_item(*start)
        if not piece:
            raise Exception('Вы не можете двигать несуществующую фигуру')
        if piece.color != board.player:
            raise Exception('Вы не можете двигать чужую фигуру')

        target = board.get_item(*end)
        if target and target.color == piece.color:
            raise Exception('Вы не можете атаковать свои фигуры')

        if not hasattr(piece, 'can_move') or not piece.can_move(board, *start, *end):
            raise Exception(f'Фигура {piece.char} не может так двигаться!')

        captured_piece = board.get_item(*end)
        board.move_item(*start, *end)

        if board.is_check(board.player):
            board.move_item(*end, *start)
            if captured_piece:
                board.board[end[0]][end[1]] = captured_piece
            raise Exception("Этот ход ставит вашего короля под шах!")
        board.change_player()

    except Exception as e:
        print('Ошибка:', e)
        input('Нажмите любую клавишу для продолжения...')