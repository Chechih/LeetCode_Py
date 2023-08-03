# 6. Zigzag Conversion
### 問題
The string **"PAYPALISHIRING"** is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
And then read line by line: **"PAHNAPLSIIGYIR"**

Write the code that will take a string and make this conversion given a number of rows:  

    string convert(string s, int numRows);
 ### 翻譯

字符串 **"PAYPALISHIRING"** 被以一個給定的行數以之字形模式書寫，像這樣：（您可能想要使用固定字體顯示這個模式以提高可讀性）

    P   A   H   N
    A P L S I I G
    Y   I   R
然後按行讀取： **"PAHNAPLSIIGYIR"**

請編寫代碼，根據給定的行數，將一個字符串進行轉換：

    string convert(string s, int numRows);

##### Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
##### Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
##### Example 3:
    Input: s = "A", numRows = 1
    Output: "A"
##### Constraints:
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000

### 想法
這題要觀察一下，會發現字母每 2numRows - 2次會有一次循環，如*Example 2*(numRows = 4)時，每 6 個一次循環，
如圖:  
![Example numRows](https://chechih.github.io/images/LeetCode/6_Example_numRows.jpg "Example numRows")  
那再來就好辦了，第一排的字母，都是循環的**第 0 個字**，而最後一排的字母都是循環的中間數**第[(2* numRows - 2)/ 2]個字**，  
再來處理中間的字元，如範例*Example 2*，就是中間 2 和 3行，那就需要一個迴圈，下去跑 for(1~numRows - 1), 中間的字元，然後去抓每一排的第 N 和 (2* numRows - 2) - N 的數字，如*Example 2*(numRows = 4)時，第一排抓**第 1 個**和**第 6 - 1 個**，第二排抓**第 2 個**和**第 6 - 2 個**，這樣依此類推下去。  
![Char Index](https://chechih.github.io/images/LeetCode/6_CharIndex.jpg "Char Index")  
好了，剛剛那些也只是去抓每個循環的字元，最外層還是需要一個 for 下去跑每個循環，如果沒把字元放錯位子，應該就可以解掉了。

### 解法
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):# 測試可能會只有一 直接回傳
            return s
        round_rule = 2* numRows - 2# 定義每幾個字元循環一次
        str_leg = len(s)# 字元長度
        rlt = ''#回傳值
        max_round = str_leg // round_rule + 2
        # 最多循環幾次 
        # 2是用來處理餘數部分的 
        # 因為剛好是零時不能跑回圈, 所以要有一, 然後結尾部分也要跑, 所以在加一, 
        # 多的部分會超出陣列, 所以不管他
        for j in range(0, max_round):
             #最上面
             ind = round_rule * j
             if(ind < str_leg):
                 rlt += s[ind]
        for i in range(1, numRows - 1):
            for j in range(0, max_round):
                #中間部分
                ind1 = round_rule * j - i# 中間部分可能多 i
                if(ind1 > 0 and ind1 < str_leg):
                    rlt += s[ind1]
                ind2 = round_rule * j + i
                if(ind2 > 0 and ind2 < str_leg):# 少 i
                    rlt += s[ind2]
        for j in range(0, max_round):
            #最下面
            ind = round_rule * j + round_rule // 2
            if(ind < str_leg):
                rlt += s[ind]
        return rlt
```