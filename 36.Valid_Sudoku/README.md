# 36. Valid Sudoku
### 問題
Determine if a **9 x 9** Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits **1-9** without repetition.
2. Each column must contain the digits **1-9** without repetition.
3. Each of the nine **3 x 3** sub-boxes of the grid must contain the digits **1-9** without repetition.
**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

### 翻譯
判定一個 **9 x 9** 的數獨棋盤是否有效。僅需 **根據以下規則** 驗證已填入的格子：

1. 每一行必須包含數字 **1-9**，且不能重複。
2. 每一列必須包含數字 **1-9**，且不能重複。
3. 棋盤的九個 **3 x 3** 子區塊中的每一個必須包含數字 **1-9**，且不能重複。
**注意：**

- 一個數獨棋盤（部分填充）可以是有效的，但不一定可解。
- 只需要根據上述規則驗證已填入的格子。

##### Example 1:
    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

![Example 1 board](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png "Example 1 board")  
圖片來源: [LeetCode](https://leetcode.com/problems/valid-sudoku/)  

##### Example 2:
    Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

##### Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.

### 想法
這題只需要去檢查每一個數字，直排、橫排、九方格內，是否有和被選中的數字相同的數字就可以了。
### 解法
```python
class Solution:
    def find_repeat(self, board_row: List[str]) -> bool:
        '''
        找重複的數字
        '''
        temp = ''
        for b in board_row:
            if b == '.':
                continue
            elif b == temp:
                return False
            else:
                temp = b
        return True
    def check_sudoku_horizontal(self, board: List[List[str]]) -> bool:
        '''
        檢查水平
        '''
        for i in range(len(board)):
            b = board[i]
            if not self.find_repeat(sorted(b)):
                return False
        return True
    def check_sudoku_vertical(self, board: List[List[str]]) -> bool:
        '''
        檢查垂直
        '''
        vb = [
            [board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0],board[7][0],board[8][0]],
            [board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1],board[7][1],board[8][1]],
            [board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2],board[7][2],board[8][2]],
            [board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3],board[7][3],board[8][3]],
            [board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4],board[7][4],board[8][4]],
            [board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5],board[7][5],board[8][5]],
            [board[0][6],board[1][6],board[2][6],board[3][6],board[4][6],board[5][6],board[6][6],board[7][6],board[8][6]],
            [board[0][7],board[1][7],board[2][7],board[3][7],board[4][7],board[5][7],board[6][7],board[7][7],board[8][7]],
            [board[0][8],board[1][8],board[2][8],board[3][8],board[4][8],board[5][8],board[6][8],board[7][8],board[8][8]]]
        return self.check_sudoku_horizontal(vb)
    def check_sudoku_square(self, board: List[List[str]]) -> bool:
        '''
        檢查九方格
        '''
        sb = [
            [board[0][0],board[1][0],board[2][0],board[0][1],board[1][1],board[2][1],board[0][2],board[1][2],board[2][2]],
            [board[0][3],board[1][3],board[2][3],board[0][4],board[1][4],board[2][4],board[0][5],board[1][5],board[2][5]],
            [board[0][6],board[1][6],board[2][6],board[0][7],board[1][7],board[2][7],board[0][8],board[1][8],board[2][8]],
            [board[3][0],board[4][0],board[5][0],board[3][1],board[4][1],board[5][1],board[3][2],board[4][2],board[5][2]],
            [board[3][3],board[4][3],board[5][3],board[3][4],board[4][4],board[5][4],board[3][5],board[4][5],board[5][5]],
            [board[3][6],board[4][6],board[5][6],board[3][7],board[4][7],board[5][7],board[3][8],board[4][8],board[5][8]],
            [board[6][0],board[7][0],board[8][0],board[6][1],board[7][1],board[8][1],board[6][2],board[7][2],board[8][2]],
            [board[6][3],board[7][3],board[8][3],board[6][4],board[7][4],board[8][4],board[6][5],board[7][5],board[8][5]],
            [board[6][6],board[7][6],board[8][6],board[6][7],board[7][7],board[8][7],board[6][8],board[7][8],board[8][8]]]
        return self.check_sudoku_horizontal(sb)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_sudoku_horizontal(board) and self.check_sudoku_vertical(board) and self.check_sudoku_square(board)
```