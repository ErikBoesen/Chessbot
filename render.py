from enum import IntEnum

class Color(IntEnum):
    WHITE = 0
    BLACK = 1

class Rank(IntEnum):
    KING = 0
    QUEEN = 1
    ROOK = 2
    BISHOP = 3
    KNIGHT = 4
    PAWN = 5

class Piece:
    color: Color
    rank: Rank

    def __init__(self, color: Color, rank: Rank):
        self.color = color
        self.rank = rank


board_start = [
    [Piece(Color.BLACK, Rank.ROOK), Piece(Color.BLACK, Rank.KNIGHT), Piece(Color.BLACK, Rank.BISHOP), Piece(Color.BLACK, Rank.QUEEN),
     Piece(Color.BLACK, Rank.KING), Piece(Color.BLACK, Rank.BISHOP), Piece(Color.BLACK, Rank.KNIGHT), Piece(Color.BLACK, Rank.ROOK)],
    [Piece(Color.BLACK, Rank.PAWN), Piece(Color.BLACK, Rank.PAWN), Piece(Color.BLACK, Rank.PAWN), Piece(Color.BLACK, Rank.PAWN),
     Piece(Color.BLACK, Rank.PAWN), Piece(Color.BLACK, Rank.PAWN), Piece(Color.BLACK, Rank.PAWN), Piece(Color.BLACK, Rank.PAWN)],
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [Piece(Color.WHITE, Rank.PAWN), Piece(Color.WHITE, Rank.PAWN), Piece(Color.WHITE, Rank.PAWN), Piece(Color.WHITE, Rank.PAWN),
     Piece(Color.WHITE, Rank.PAWN), Piece(Color.WHITE, Rank.PAWN), Piece(Color.WHITE, Rank.PAWN), Piece(Color.WHITE, Rank.PAWN)],
    [Piece(Color.WHITE, Rank.ROOK), Piece(Color.WHITE, Rank.KNIGHT), Piece(Color.WHITE, Rank.BISHOP), Piece(Color.WHITE, Rank.QUEEN),
     Piece(Color.WHITE, Rank.KING), Piece(Color.WHITE, Rank.BISHOP), Piece(Color.WHITE, Rank.KNIGHT), Piece(Color.WHITE, Rank.ROOK)],
]

UNICODE_START = 0x2654
BLACK_OFFSET = 0x6

def render_piece(piece):
    if piece is None:
        return ' '
    return chr(UNICODE_START + (BLACK_OFFSET * piece.color) + piece.rank)

def render_board(board):
    return '\n'.join([''.join([render_piece(piece) for piece in row]) for row in board])

print(render_board(board_start))
