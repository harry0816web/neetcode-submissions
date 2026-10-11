class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            row_set = set()
            for j in range(0, 9):
                if board[i][j] == '.': continue

                if board[i][j] not in row_set:
                    row_set.add(board[i][j])
                else:
                    return False

        for i in range(0, 9):
            column_set = set()
            for j in range(0, 9):
                if board[j][i] == '.': continue
                
                if board[j][i] not in column_set:
                    column_set.add(board[j][i])
                else:
                    return False

        for block_i in range(0, 9, 3):
            for block_j in range(0, 9, 3):
                block_set = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[block_i + i][block_j + j] == '.': continue

                        if board[block_i + i][block_j + j] not in block_set:
                            block_set.add(board[block_i + i][block_j + j]) 
                        else:
                            return False


        return True