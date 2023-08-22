# 13. Roman to Integer
### 問題
Roman numerals are represented by seven different symbols: **I**, **V**, **X**, **L**, **C**, **D** and **M**.
<pre>
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
</pre>
For example, **2** is written as **II** in Roman numeral, just two ones added together. **12** is written as **XII**, which is simply **X + II**. The number **27** is written as **XXVII**, which is **XX + V + II**.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not **IIII**. Instead, the number four is written as **IV**. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as **IX**. There are six instances where subtraction is used:

**I** can be placed before **V** (5) and **X** (10) to make 4 and 9. 
**X** can be placed before **L** (50) and **C** (100) to make 40 and 90. 
**C** can be placed before **D** (500) and **M** (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
 ### 翻譯
羅馬數字由七種不同的符號表示：**I**、**V**、**X**、**L**、**C**、**D** 和 **M**。
<pre>
符號          數值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
</pre>
例如，數字 **2** 用羅馬數字表示為 **II**，只是將兩個 1 相加。數字 **12** 表示為 **XII**，即 **X + II**。數字 **27** 表示為 **XXVII**，即 **XX + V + II**。

羅馬數字通常由左到右，從大到小進行書寫。然而，數字四的羅馬表示不是 **IIII**，而是 **IV**。這是因為 1 出現在 5 之前，所以要將其減去，得到四。同樣的原則適用於數字九，即 **IX**。有六種情況下使用減法：

**I** 可以放在 **V**（5）和 **X**（10）之前，以形成 4 和 9。
**X** 可以放在 **L**（50）和 **C**（100）之前，以形成 40 和 90。
**C** 可以放在 **D**（500）和 **M**（1000）之前，以形成 400 和 900。
給定一個羅馬數字，將其轉換成整數。
##### Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.
##### Example 2:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
##### Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
##### Constraints:
- 1 <= s.length <= 15
- **s** contains only the characters **('I', 'V', 'X', 'L', 'C', 'D', 'M')**.
- It is **guaranteed** that **s** is a valid roman numeral in the range [1, 3999].

### 想法 
這題也可以建個羅馬字母對數字的表，如下:  
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
建完之後直接設定個變數用來加總用，然後開始掃字串，把掃到的數字直接轉成數字加總，只是掃的時候要注意，上一個是不是比現在小，如果是，可能就是 4(IV), 9:(IX), 40(XL)等等的羅馬數字，必須把上一個減掉，這段可以把它做成全部數字加起來，遇到時減兩次，因為之前有先加了。
### 解法 
```python
class Solution:
    symbols = {# 對照表
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    def romanToInt(self, s: str) -> int:
        symbols = self.symbols
        rlt = 0
        prev_val = 0# 上一個值
        for c in s:
            val = symbols[c]
            if val > prev_val:
                # 如果現在的數字比上個大，代表可能是 4(IV) 9(IX)，這種要減去的羅馬數字
                rlt -= 2 * prev_val
                # 減 2 倍是因為上一個回圈是加的，扣掉
            rlt += val
            prev_val = val
        return rlt
```