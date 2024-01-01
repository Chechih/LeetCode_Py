# 43. Multiply Strings
### 問題
Given two non-negative integers **num1** and **num2** represented as strings, return the product of **num1** and **num2**, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

### 翻譯
給定兩個非負整數 **num1** 和 **num2**，以字串表示，返回它們的乘積，同樣以字串表示。

**注意：** 你不能使用任何內建的 BigInteger 函式庫或直接將輸入轉換為整數。

##### Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

##### Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

##### Constraints:
- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only.
- Both num1 and num2 do not contain any leading zero, except the number 0 itself.

### 想法
這題是限制不能使用任何內建的 BigInteger 函式庫或直接將輸入轉換為整數，但看起來他的限制是你只能用一位數的乘法，做法可以歸類為:
1. 先建立一個陣列，陣列大小 num1 和 num2 的大小減一就可以了，因為最後一個數字會自己進位
2. 然後根據乘法相乘的公式，直接用迴圈相乘，但每次只做一位數
3. 再來就是要考慮，每個數字相乘時，可能會溢位，大於 10，要進位
4. 然後再來就是把陣列轉成字串
5. 還有考慮全部是 0 的狀況，因為不可能傳會 '0000000....', 這東西，必須把它變成 '0'
### 解法 1
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_leg = len(num1)
        num2_leg = len(num2)
        ans = [0] * (num1_leg + num2_leg  -1)

        for i in range(num1_leg -1, -1, -1):
            n1 = int(num1[i])
            for j in range(num2_leg -1, -1, -1):
                ans[i + j] = ans[i + j] + n1 * int(num2[j])
        
        for i in range(num1_leg + num2_leg -1 - 1, 0, -1):
            ans[i - 1] = ans[i - 1] + ans[i] //10
            ans[i] = ans[i] % 10
        
        ans = [str(a) for a in ans]
        rlt = ''.join(ans)

        return rlt if rlt != '0' * (num1_leg + num2_leg  -1) else '0'
        # 這邊式判斷如果全部是 '0' 不要傳回 '0000...', 而是傳回 '0'
```