def init_board(b):
    Rook(b, (1, 1), "W")
    Knight(b, (1, 2), "W")
    Bishop(b, (1, 3), "W")
    King(b, (1, 4), "W")
    Queen(b, (1, 5), "W")
    Bishop(b, (1, 6), "W")
    Knight(b, (1, 7), "W")
    Rook(b, (1, 8), "W")

    Pawn(b, (2, 1), "W")
    Pawn(b, (2, 2), "W")
    Pawn(b, (2, 3), "W")
    Pawn(b, (2, 4), "W")
    Pawn(b, (2, 5), "W")
    Pawn(b, (2, 6), "W")
    Pawn(b, (2, 7), "W")
    Pawn(b, (2, 8), "W")

    Rook(b, (8, 1), "B")
    Knight(b, (8, 2), "B")
    Bishop(b, (8, 3), "B")
    King(b, (8, 4), "B")
    Queen(b, (8, 5), "B")
    Bishop(b, (8, 6), "B")
    Knight(b, (8, 7), "B")
    Rook(b, (8, 8), "B")

    Pawn(b, (7, 1), "B")
    Pawn(b, (7, 2), "B")
    Pawn(b, (7, 3), "B")
    Pawn(b, (7, 4), "B")
    Pawn(b, (7, 5), "B")
    Pawn(b, (7, 6), "B")
    Pawn(b, (7, 7), "B")
    Pawn(b, (7, 8), "B")


class Board:

    def __init__(self):
        self.__board = {(i, j): "----" for i in range(1, 9) for j in range(1, 9)}

    def __setitem__(self, key, value):
        self.__board[key] = value

    def __getitem__(self, pos):
        return self.__board[pos]

    def __str__(self):
        board_repr = ""
        counter = 0
        for key, item in self.__board.items():
            board_repr += f" {item} "
            counter += 1
            if counter == 8:
                counter = 0
                board_repr += "\n"
        return board_repr

    def clear_pos(self, piece):
        self[piece.position] = "---"


class Piece:
    def __init__(self, board: Board, position: tuple[int, int], symbol: str, color: str):
        self.position = position
        self.symbol = symbol
        self.color = color
        self.board = board
        board.__setitem__(position, self)

    def move(self, new_position):
        self.board.clear_pos(self)
        self.position = new_position
        self.board[new_position] = f"({self.color}{self.symbol})"

    def __repr__(self):
        return f"({self.color}{self.symbol})"


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
        super().__init__(board, position, "T", color)


class Rook(Piece):
    def __init__(self, board: Board, position: tuple[int, int], color: str):
        super().__init__(board, position, "R", color)


class Pawn(Piece):
    def __init__(self, board: Board, position: tuple[int, int], color: str):
        super().__init__(board, position, "P", color)


def main():
    board = Board()
    init_board(board)

    board[(1, 4)].move((4, 4))
    board[(1, 5)].move((4, 3))
    board[(1, 6)].move((6, 4))
    board[(1, 7)].move((8, 4))
    board[(1, 8)].move((5, 4))
    board[(8, 2)].move((4, 7))
    print(board)


if __name__ == "__main__":
    main()
