class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        board_set = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue
                if board[i][j] in row_set[i] or board[i][j] in col_set[j] or board[i][j] in board_set[(i//3,j//3)]:
                    return False
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                board_set[(i//3,j//3)].add(board[i][j])
        
        return True
                

        