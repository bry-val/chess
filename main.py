def init_board(b):
    King(b, (1, 5), "W")
    King(b, (8, 5), "B")
    Queen(b, (1, 5), "W")
    Queen(b, (8, 5), "B")
    Bishop(b, (1, 5), "W")
    Bishop(b, (8, 5), "B")
    Rook(b, (1, 5), "W")
    Rook(b, (8, 5), "B")
    Pawn(b, (1, 5), "W")
    Pawn(b, (8, 5), "B")


class Board:

    def __init__(self):
        self.board = {(i, j): "." for i in range(1, 9) for j in range(1, 9)}

    def __setitem__(self, key, value):
        self.board[key] = value

    def __str__(self):
        board_repr = ""
        counter = 0
        for key, item in self.board.items():
            board_repr += f" {item} "
            counter += 1
            if counter == 8:
                counter = 0
                board_repr += "\n"
        return board_repr


class Piece:
    def __init__(self, board: Board, position: tuple[int, int], symbol: str, color: str):
        self.position = position
        self.symbol = symbol
        self.color = color
        board[position] = f"({color}{symbol})"

    def move(self):
        pass


class King(Piece):
    def __init__(self, board: Board, position: tuple[int, int], color: str):
        super().__init__(board, position, "K", color)


class Queen(Piece):
    def __init__(self, board: Board, position: tuple[int, int], color: str):
        super().__init__(board, position, "Q", color)


class Bishop(Piece):
    def __init__(self, board: Board, position: tuple[int, int], color: str):
        super().__init__(board, position, "B", color)


class Knight(Piece):
    def __init__(self, board: Board, position: tuple[int, int], color: str):
        super().__init__(board, position, "G", color)


class Rook(Piece):
    def __init__(self, board: Board, position: tuple[int, int], color: str):
        super().__init__(board, position, "R", color)


class Pawn(Piece):
    def __init__(self, board: Board, position: tuple[int, int], color: str):
        super().__init__(board, position, "P", color)


def main():
    board = Board()
    init_board(board)

    print(board)


if __name__ == "__main__":
    main()
