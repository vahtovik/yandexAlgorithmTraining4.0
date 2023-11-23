class QueenPlacement:
    COUNTER = 0

    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def put_next_queen(self, col):
        if col >= self.n:
            self.COUNTER += 1
            return
        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.put_next_queen(col + 1)
                self.board[row][col] = 0


n = int(input())

if __name__ == '__main__':
    res = QueenPlacement(n)
    res.put_next_queen(0)
    print(res.COUNTER)
