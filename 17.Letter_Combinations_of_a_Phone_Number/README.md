# 17. Letter Combinations of a Phone Number
### 問題
Given a string containing digits from **2-9** inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 ### 翻譯
給定一個包含 **2 到 9** 之間數字的字符串，返回該數字可能表示的所有可能字母組合。答案可以以**任何順序**返回。

以下給出了數字到字母的映射（就像在電話按鈕上一樣）。請注意，數字 1 不對應任何字母。
![Phone Number](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png "Phone Number")  
圖片來源: [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)  
##### Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
##### Example 2:
    Input: digits = ""
    Output: []
##### Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

##### Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

### 想法 
這題可以使用遞迴來解，先建立一個對照表，用來數字對英文，然後跑遞迴，把可能的組合存起來即可。
EX: Input '23', 先除取  
2 ('a') -> 3('d', 'e', 'f'),  
2 ('b') -> 3('d', 'e', 'f'),   
2 ('c') -> 3('d', 'e', 'f')  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
### 解法 
```python
class Solution:
    rule = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def gather(self, letters: List[int], digits: str, thisTxt: str = '') -> None:
        if(len(digits) < 1):
            letters.append(thisTxt)# 如果 digits 都消耗完畢，將蒐集的字母存起來
            return
        for m in self.rule[digits[0]]:# 取出一個數字開始跑有可能的字母
            self.gather(letters, digits[1::], thisTxt + m)
    
    def letterCombinations(self, digits: str) -> List[str]:
        rlt = []
        if digits != '':# 空的直接不跑
            self.gather(rlt, digits)
        
        return rlt
```