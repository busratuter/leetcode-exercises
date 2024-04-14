class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        direction = 1
        row = 0

        for char in s:
            rows[row] += char
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction

        return ''.join(rows)
