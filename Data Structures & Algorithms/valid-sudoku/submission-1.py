class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # block = (row / 3) * 3 + (col / 3)
        # => i, j -> row_sets[i], column_sets[j], block_sets[(i / 3) * 3 + (j / 3)]
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        block_sets = [set() for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                num = board[i][j]
                if num == '.': continue

                if num not in row_sets[i]:
                    row_sets[i].add(num)
                else: return False

                if num not in col_sets[j]:
                    col_sets[j].add(num)
                else: return False

                block_id = ((i // 3) * 3 + (j // 3))
                # print(i, j, block_id, sep=", ")
                if num not in block_sets[block_id]:
                    block_sets[block_id].add(num)
                else: return False


        return True