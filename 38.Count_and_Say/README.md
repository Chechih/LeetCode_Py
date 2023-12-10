# 38. Count and Say
### 問題
The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

- **countAndSay(1) = "1"**
- **countAndSay(n)** is the way you would "say" the digit string from **countAndSay(n-1)**, which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the **minimal** number of substrings such that each substring contains exactly **one** unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string **"3322251"**:

Given a positive integer **n**, return the **n<sup>th</sup>** term of the **count-and-say** sequence.

### 翻譯
**數數說** 序列是一個由遞迴公式定義的數位字串序列：

**countAndSay(1) = "1"**
**countAndSay(n)** 的說法就是你會從 **countAndSay(n-1)** 的數位字串中"說"出來，然後轉換成一個不同的數位字串。
要確定如何"說"一個數位字串，將它分成 **最小的** 子字串，每個子字串正好包含 **一個** 唯一的數位。然後對於每個子字串，說出數位的數量，然後說出該數位。最後，連接每個說出的數位。
例如，對於數位字串 **"3322251"** 的說法和轉換：

給定一個正整數 **n**，返回 **數數說** 序列的第 **n<sup>th</sup>** 項。

![Example 1 Count_and_Say](https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg "Example 1 Count_and_Say")  
圖片來源: [LeetCode](https://leetcode.com/problems/count-and-say/)  

##### Example 1:
    Input: n = 1
    Output: "1"
    Explanation: This is the base case.

##### Example 2:
    Input: n = 4
    Output: "1211"
    Explanation:
    countAndSay(1) = "1"
    countAndSay(2) = say "1" = one 1 = "11"
    countAndSay(3) = say "11" = two 1's = "21"
    countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

##### Constraints:
- 1 <= n <= 30

### 想法
這題其實題目要理解下XDDD  
看得蠻久的......  
不過看懂後，其實他就是把前一個數字說出來，比如例子 2 中
n = 2 就是說出 n = 1 的數字， 1 是 '1'， 那 n = 2 就是說 1 個 1， --> 11  
n = 3 就是說出 n = 2 的數字， 2 是 '11'，那 n = 3 就是說 2 個 1， --> 21  
n = 4 就是說出 n = 3 的數字， 3 是 '21'，那 n = 4 就是說 1 個 2，1 個 1 --> 1211  
依此類推  
所以可以寫個迴圈，從 2 開始跑到 n 就可以求出答案出來了，因為 1 就是 1(好繞)。  

### 解法
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        rlt = '1'
        for _ in range(2, n + 1):
            res = ''
            val = rlt[0]
            # 計錄數字是否相同用
            count = 0
            # 計數用
            for s in rlt:
                if(val == s):
                    count += 1
                    # 累加
                else:
                    res += str(count) + val
                    # 開始說數字
                    val = s
                    count = 1
                    # 初始
            res += str(count) + val
            rlt = res
            # 記錄每一輪的值

        return rlt
```