# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = {}
        
        for h in range(9):
            for v in range(9):
                current = board[h][v]
                if not current.isdigit():
                    continue

                if (h+1)*10 not in sudoku:
                    sudoku[(h+1)*10] = {current}
                else:
                    if current in sudoku[(h+1)*10]:
                        return False
                    sudoku[(h+1)*10].add(current)
                    
                if v+1 not in sudoku:
                    sudoku[v+1] = {current}
                else:
                    if current in sudoku[v+1]:
                        return False
                    sudoku[v+1].add(current)

                if (h//3, v//3) not in sudoku:
                    sudoku[(h//3, v//3)] = {current}
                else:
                    if current in sudoku[(h//3, v//3)]:
                        return False
                    sudoku[(h//3, v//3)].add(current)
                
        return True

# |5|3| | |7| | | | |
# |6| | |1|9|5| | | |
# | |9|8| | | | |6| |
# |8| | | |6| | | |3|
# |4| | |8| |3| | |1|
# |7| | | |2| | | |6|
# | |6| | | | |2|8| |
# | | | |4|1|9| | |5|
# | | | | |8| | |7|9|


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]
sln = Solution()
assert sln.isValidSudoku(board) is True
