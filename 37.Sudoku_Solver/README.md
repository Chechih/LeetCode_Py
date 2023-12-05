# 37. Sudoku Solver
### 問題
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits **1-9** must occur exactly once in each row.
2. Each of the digits **1-9** must occur exactly once in each column.
3. Each of the digits **1-9** must occur exactly once in each of the 9 **3x3** sub-boxes of the grid.
The **'.'** character indicates empty cells.

### 翻譯
撰寫一個程式來通過填充空白格子來解決數獨。

一個數獨解必須滿足 **以下所有規則**：

1. 每個數字 **1-9** 在每一行中必須恰好出現一次。
2. 每個數字 **1-9** 在每一列中必須恰好出現一次。
3. 每個數字 **1-9** 在棋盤的每個 9 個 **3x3** 子區塊中必須恰好出現一次。
字符 **'.'** 表示空白格子。

##### Example 1:
    Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    Explanation: The input board is shown above and the only valid solution is shown below:

![Example 1 board](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png "Example 1 board")  
![Example 1 board answer](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png "Example 1 board answer")  
圖片來源: [LeetCode](https://leetcode.com/problems/sudoku-solver/)  

##### Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'.
- It is guaranteed that the input board has only one solution.

### 想法
這題是要求數獨的解，可以一開始把每個需要填的位置，把可能的數字都先找出來，再遞迴去把這些可能的數字都帶帶看，直到找出答案。帶入時只要檢查直軸和橫軸，和九方格內有沒有重複的就好，如果有重複就換下一個數字試試，如果所有可能都試過了代表前面找錯了，就必須回朔檢查前面的數字，這樣把所有數字找過找即可。
### 解法
```python
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
```