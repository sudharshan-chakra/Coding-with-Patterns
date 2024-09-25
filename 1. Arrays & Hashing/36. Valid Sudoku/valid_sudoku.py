class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols = len(board),len(board[0])

        row_set = [set() for _ in range(rows)]
        col_set = [set() for _ in range(cols)]
        grid_set = [[set() for _ in range(cols//3)] for _ in range(rows//3)]

        for r in range(rows):
            for c in range(cols):
                cur = board[r][c]
                if cur == ".":
                    continue
                if cur in row_set[r] or cur in col_set[c] or cur in grid_set[r//3][c//3]:
                    return False
                row_set[r].add(cur)
                col_set[c].add(cur)
                grid_set[r//3][c//3].add(cur)

        return True