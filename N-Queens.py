def dfs_n_queens(n: int):
    if n < 1:
        return []

    solutions = []
    board = []

    def is_safe(row, column):
        for previous_row, previous_column in enumerate(board):

            # Same column
            if previous_column == column:
                return False

            # Same diagonal
            if abs(previous_row - row) == abs(previous_column - column):
                return False

        return True

    def dfs(row):
        # All rows have a queen: we found a solution
        if row == n:
            solutions.append(board.copy())
            return

        # Try every column in the current row
        for column in range(n):
            if is_safe(row, column):
                board.append(column)

                dfs(row + 1)

                # Undo the placement (backtracking)
                board.pop()

    dfs(0)

    return solutions
