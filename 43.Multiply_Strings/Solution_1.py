
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



solution = Solution()
print(solution.multiply("9133", "0"))