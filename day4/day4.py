import numpy as np


class BingoBoard:
    def __init__(self, board):
        self.board = np.fromstring(board, sep='\n', dtype=int).reshape((5, 5))
        self.marked = []

    def mark_number(self, n):
        if n in self.board:
            self.marked.append(n)
            return self.check_board()
        return False

    def get_score(self):
        return sum(np.setdiff1d(self.board, self.marked))

    def check_board(self):
        cols = np.split(self.board, self.board.shape[1], axis=1)
        rows = np.split(self.board, self.board.shape[1], axis=0)
        return any([np.isin(chunk, self.marked).all() for chunk in cols + rows])


def get_data(filename):
    with open(filename) as file:
        numbers, *boards = file.read().split("\n\n")

        numbers = [int(n) for n in numbers.split(",")]
        boards = [BingoBoard(board) for board in boards]
        return numbers, boards


def day4(numbers, boards):
    winning_score = None
    for n in numbers:
        boards_to_remove = set()
        for board in boards:
            if board.mark_number(n):
                boards_to_remove.add(board)
                if not winning_score:
                    winning_score = board.get_score() * n
                elif len(boards) == 1:
                    losing_score = board.get_score() * n
                    return winning_score, losing_score
        boards = [board for board in boards if board not in boards_to_remove]


if __name__ == '__main__':
    nbrs, boards = get_data('day4.txt')
    p1, p2 = day4(nbrs, boards)

    print(f'part1: {p1}, part2: {p2}')
