# 12. Integer to Roman
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
For example, **2** is written as **II** in Roman numeral, just two one's added together. **12** is written as **XII**, which is simply **X + II**. The number **27** is written as **XXVII**, which is **XX + V + II**.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not **IIII**. Instead, the number four is written as **IV**. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as **IX**. There are six instances where subtraction is used:

**I** can be placed before **V** (5) and **X** (10) to make 4 and 9. 
**X** can be placed before **L** (50) and **C** (100) to make 40 and 90. 
**C** can be placed before **D** (500) and **M** (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
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
例如，**2** 用羅馬數字表示為 **II**，即兩個 1 相加。**12** 表示為 **XII**，即 **X + II**。數字 **27** 表示為 **XXVII**，即 **XX + V + II**。

羅馬數字通常由左到右從大到小進行書寫。然而，數字四並不是 **IIII**，而是 **IV**。這是因為 1 出現在 5 之前，所以要減去它得到四。同樣的原則適用於數字九，即 **IX**。有六種情況下使用減法：

**I** 可以放在 **V**（5）和 **X**（10）之前，以形成 4 和 9。
**X** 可以放在 **L**（50）和 **C**（100）之前，以形成 40 和 90。
**C** 可以放在 **D**（500）和 **M**（1000）之前，以形成 400 和 900。
給定一個整數，將其轉換成羅馬數字。
##### Example 1:
    Input: num = 3
    Output: "III"
    Explanation: 3 is represented as 3 ones.
##### Example 2:
    Input: num = 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.
##### Example 3:
    Input: num = 1994
    Output: "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
##### Constraints:
- 1 <= num <= 3999

### 想法 
這題只需要建個數字對羅馬字母的表，如下:  
        1000: 'M',  
        900: 'CM',  
        500: 'D',  
        400: 'CD',  
        100: 'C',
        90: 'XC',  
        50: 'L',  
        40: 'XL',  
        10: 'X',  
        9: 'IX',  
        5: 'V',  
        4: 'IV',  
        1: 'I',  
然後用除法除除看，商是不是大於 0，大於 0 的話代表至少有一個此字母，然後 for 下去跑加此字母，一直把表跑完即可。  
補充: 因為表是大到小，所以不會出現 9 變成 IIIIIIIII 狀況。
### 解法 
```python
class Solution:
    symbols = {# 對照表
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    def intToRoman(self, num: int) -> str:
        symbols = self.symbols
        rlt = ''
        for n, s in symbols.items():
            divide = num // n# 除除看，能除代表至少有一個此字母
            if divide != 0:
                for _ in range(divide):# 循環加字母
                    rlt += s
                num %= n

        return rlt
```