from typing import List
from typing import Set
from typing import Dict
from typing import Tuple

class Solution:
    sudoku_square_keys = [
        [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)], 
        [(0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)], 
        [(0, 6), (1, 6), (2, 6), (0, 7), (1, 7), (2, 7), (0, 8), (1, 8), (2, 8)], 
        [(3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (5, 2)], 
        [(3, 3), (4, 3), (5, 3), (3, 4), (4, 4), (5, 4), (3, 5), (4, 5), (5, 5)], 
        [(3, 6), (4, 6), (5, 6), (3, 7), (4, 7), (5, 7), (3, 8), (4, 8), (5, 8)], 
        [(6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (8, 1), (6, 2), (7, 2), (8, 2)], 
        [(6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5)], 
        [(6, 6), (7, 6), (8, 6), (6, 7), (7, 7), (8, 7), (6, 8), (7, 8), (8, 8)]]
    def sudoku_horizontal_answer(self, board: List[List[str]]) -> Set[str]:
        '''
        檢查水平可能的數字
        '''
        rlt = {}
        for i in range(9):
            b = board[i]
            no_point = {k for k in b if k != '.'}
            possibility_val = self.xor(no_point)
            for j in range(9):
                if(b[j] == '.'):
                    rlt[(i, j)] = possibility_val
        return rlt
    def xor(self, remove_items: Set[str]) -> Set[str]:
        return {'1', '2', '3', '4', '5', '6', '7', '8', '9'} ^ remove_items
    def sudoku_vertical_answer(self, board: List[List[str]]) -> Set[str]:
        '''
        檢查垂直可能的數字
        '''
        rlt = {}
        for i in range(9):
            no_point = {k[i] for k in board if k[i] != '.'}
            possibility_val = self.xor(no_point)
            for j in range(9):
                if(board[j][i] == '.'):
                    rlt[(j, i)] = possibility_val
        return rlt
    def sudoku_square_answer(self, board: List[List[str]]) -> Set[str]:
        '''
        檢查九方格可能的數字
        '''
        rlt = {}
        keys = self.sudoku_square_keys
        for i in range(9):
            no_point = {board[k[0]][k[1]] for k in keys[i] if board[k[0]][k[1]] != '.'}
            possibility_val = self.xor(no_point)
            for j in range(9):
                k = keys[i][j]
                if(board[k[0]][k[1]] == '.'):
                    rlt[k] = possibility_val
        return rlt

    def possibility_answer(self, board: List[List[str]])-> Dict[Tuple[int, int], Set[str]]:
        '''
        確認每一格可能的數字
        '''
        ha = self.sudoku_horizontal_answer(board)
        va = self.sudoku_vertical_answer(board)
        sa = self.sudoku_square_answer(board)  
        return { i: vals & va[i] & sa[i] for i, vals in ha.items() }
    def is_valid(self, board: List[List[str]], i: int, j: int, val: str)-> bool:
        for k in range(9):
            if board[k][j] == val:
                return False
            if board[i][k] == val:
                return False
            row = i // 3 * 3 + k // 3
            col = j // 3 * 3 + k % 3
            if board[row][col] == val:
                return False
        return True
    def check_answer(self, possibility_answer: Dict[Tuple[int, int], Set[str]], board: List[List[str]]) -> bool:
        if not possibility_answer:
            return True
        last_key = list(possibility_answer)[-1]
        pv = possibility_answer[last_key]
        x, y = last_key
        del possibility_answer[last_key]
        for v in pv:
            if not self.is_valid(board, x, y, v):
                continue
            board[x][y] = v
            if (self.check_answer(possibility_answer, board)):
                return True
            board[x][y] = '.'
        possibility_answer[last_key] = pv
        return False
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pa = self.possibility_answer(board)
        self.check_answer(pa, board)
        return


board = [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]
solution = Solution()
solution.solveSudoku(board)   