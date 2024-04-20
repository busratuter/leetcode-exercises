class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_key = f"row_{i}_{board[i][j]}"
                    col_key = f"col_{j}_{board[i][j]}"
                    box_key = f"box_{i//3}_{j//3}_{board[i][j]}"
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    seen.update([row_key, col_key, box_key])
        return True
