# 8. String to Integer (atoi)
### 問題
Implement the **myAtoi(string s)** function, which converts a string to a 32-bit signed integer (similar to C/C++'s **atoi** function).

The algorithm for **myAtoi(string s)** is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is **'-'** or **'+'**. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. **"123" -> 123**, **"0032" -> 32**). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range **[-2<sup>31</sup>, 2<sup>31</sup> - 1]**, then clamp the integer so that it remains in the range. Specifically, integers less than **-2<sup>31</sup>** should be clamped to **-2<sup>31</sup>**, and integers greater than **2<sup>31</sup> - 1** should be clamped to **2<sup>31</sup> - 1**.
6. Return the integer as the final result.
 ### 翻譯
請實現 **myAtoi(string s)** 函數，它將一個字符串轉換成一個 32 位帶符號整數（類似於 C/C++ 中的 **atoi** 函數）。

**myAtoi(string s)** 函數的算法如下：

1. 讀取並忽略任何前導空格。
2. 檢查下一個字符（如果還沒有到達字符串的末尾）是否為 '-' 或 '+'。如果是其中之一，則將其讀取。這決定了最終結果的正負性。如果都不出現，則假設結果是正數。
3. 讀取下一個字符，直到遇到下一個非數字字符或到達輸入的末尾。忽略字符串的其餘部分。
4. 將這些數字轉換成整數（例如，**"123" -> 123**，**"0032" -> 32**）。如果沒有讀取到數字，則整數為 0。根據步驟 2，調整正負號。
5. 如果整數超出了 32 位帶符號整數的範圍 [-2<sup>31</sup>, 2<sup>31</sup> - 1]，則將整數夾縮到該範圍內。具體來說，小於 **-2<sup>31</sup>** 的整數應夾縮為 **-2<sup>31</sup>**，大於 **2<sup>31</sup> - 1** 的整數應夾縮為 **2<sup>31</sup> - 1**。
6. 將整數作為最終結果返回。

##### Example 1:
    Input: s = "42"
    Output: 42
    Explanation: The underlined characters are what is read in, the caret is the current reader position.
    Step 1: "42" (no characters read because there is no leading whitespace)
            ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
            ^
    Step 3: "42" ("42" is read in)
            ^
    The parsed integer is 42.
    Since 42 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 42.
##### Example 2:
    Input: s = "   -42"
    Output: -42
    Explanation:
    Step 1: "   -42" (leading whitespace is read and ignored)
                ^
    Step 2: "   -42" ('-' is read, so the result should be negative)
                ^
    Step 3: "   -42" ("42" is read in)
                ^
    The parsed integer is -42.
    Since -42 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is -42.
##### Example 3:
    Input: s = "4193 with words"
    Output: 4193
    Explanation:
    Step 1: "4193 with words" (no characters read because there is no leading whitespace)
            ^
    Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
            ^
    Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
                ^
    The parsed integer is 4193.
    Since 4193 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 4193.
##### Constraints:
- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

### 想法
其實這題解題不皺都寫出來了!?跟著它寫出來的不皺寫基本上沒有太大的問題，只是要測一下，和想可能的測資。  
最終整理出來的步驟為:  
1.刪除處理左右空白  
2.檢查正負號，正號可以不理他，負號之後要把數字弄成負號  
3.開始獨字串，判斷數字，只要讀到不是數字的直接捨棄  
4.將剛剛讀取到符合的字串，直接轉成數字  
5.如果比 -2<sup>31</sup> 小，回傳 -2<sup>31</sup>，比 2<sup>31</sup> 大，回傳 2<sup>31</sup>，其餘回傳剛剛轉成的數字  

### 解法
```python
class Solution:
    max_size = 2 ** 31 - 1#32 位元最大值
    min_size = -max_size - 1 #32 位元最小值
    def is_number(self, c: str)-> bool:
        '''
        檢查 char 是不是數字
        '''
        return c >= '0' and c <= '9'
    def myAtoi(self, s: str) -> int:
        s = s.strip()#字串左右兩邊空格拿掉
        rlt_s = ''
        if s.startswith('+'):#檢查正號
            s = s[1:]
        elif s.startswith('-'):#檢查負號
            s = s[1:]
            rlt_s = '-'
        for c in s:
            if self.is_number(c):
                rlt_s += c
            else:
                break
        if rlt_s == '' or rlt_s == '-':
            return 0
        rlt = int(rlt_s)
        if(rlt > self.max_size):
            return self.max_size
        elif(rlt < self.min_size):
            return self.min_size
        else:
            return rlt
```