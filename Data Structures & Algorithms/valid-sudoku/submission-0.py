class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = {}

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue
                
                if value in rows[r]:
                    return False
                rows[r].add(value)

                if value in cols[c]:
                    return False
                cols[c].add(value)

                cur_box = (r // 3, c // 3)

                if cur_box not in box:
                    box[cur_box] = set()
                
                if value in box[cur_box]:
                    return False
                
                box[cur_box].add(value)
        
        return True