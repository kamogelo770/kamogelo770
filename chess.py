class ChessBoard:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = ' '
        self.board[end_row][end_col] = piece

def main():
    board = ChessBoard()
    board.display_board()

    while True:
        start_input = input("Enter start position (row col): ")
        end_input = input("Enter end position (row col): ")

        start_row, start_col = map(int, start_input.split())
        end_row, end_col = map(int, end_input.split())

        board.move_piece((start_row, start_col), (end_row, end_col))
        board.display_board()

if __name__ == "__main__":
    main()
