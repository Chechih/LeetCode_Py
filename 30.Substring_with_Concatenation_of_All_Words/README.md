# 30. Substring with Concatenation of All Words
### 問題
You are given a string **s** and an array of strings **words**. All the strings of **words** are of **the same length**.

A **concatenated substring** in **s** is a substring that contains all the strings of any permutation of **words** concatenated.

- For example, if **words = ["ab","cd","ef"]**, then **"abcdef"**, **"abefcd"**, **"cdabef"**, **"cdefab"**, **"efabcd"**, and **"efcdab"** are all concatenated strings. **"acdbef"** is not a concatenated substring because it is not the concatenation of any permutation of **words**.
Return the starting indices of all the concatenated substrings in **s**. You can return the answer in **any order**.

### 翻譯
你被給定一個字符串 **s** 和一個字符串陣列 **words**。**words** 中的所有字符串都具有 **相同的長度**。

在 **s** 中，一個 **連接的子字符串** 是指包含了任意排列的 **words** 中所有字符串的子字符串。

- 例如，如果 **words = ["ab","cd","ef"]**，那麼 **"abcdef"**、**"abefcd"**、**"cdabef"**、**"cdefab"**、**"efabcd"** 和 **"efcdab"** 都是連接的字符串。**"acdbef"** 不是一個連接的子字符串，因為它不是任何 **words** 排列的串接。
返回 **s** 中所有連接子字符串的起始索引。答案可以以 **任何順序** 返回。

##### Example 1:
    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]
    Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
    The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
    The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
    The output order does not matter. Returning [9,0] is fine too.
##### Example 2:
    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    Output: []
    Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
    There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
    We return an empty array.\
##### Example 3:
    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]
    Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
    The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
    The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
    The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.

##### Constraints:
- 1 <= s.length <= 10<sup>4</sup>
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters.

### 想法 1
因為題目有說 **words** 裡面的字串長度都是相同的(假設長度 *word_leg*)，所以先設定一個 for 迴圈在外層跑遍 **s**，然後把 **s** 根據 *word_leg* 的長度切割，切到和 **words** 的總長度(*all_words_leg*)相等，下去比對陣列是否相等來找 Index，需要注意的部分是都需要排列才能比對陣列是否相同。
### 解法 1
```python
class Solution:
    def split_list(self, text, leg) -> List[str]:
        rlt = [text[idx : idx + leg] for idx in range(0, len(text), leg)]
        rlt.sort()
        return rlt
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        all_words_leg = len(''.join(words))
        if all_words_leg == 0:
            return []
        word_leg = len(words[0])
        #因為題目有說 words 內的 word 長度相等
        s_leg = len(s)
        words.sort()
        rlt = []
        for i in range(s_leg - all_words_leg + 1):
            split_str_list = self.split_list(s[i: i + all_words_leg ], word_leg)
            if split_str_list == words:
                #因為排序過了, 如果相等代表是所求的東西
                rlt.append(i)
        return rlt
```
### 想法 2
這是在 **想法1** 的基礎上，再使用 *set* 去儲存已經判斷過的*以切割 s*，這樣可以增加些速度，不過這應該是這想法的極限了XDDD
### 解法 2
```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        is_check_ok = set()
        # 將檢查過可以的字串存起來
        is_check_no = set()
        # 將檢查過不可以的字串存起來
        def split_list(text, leg) -> List[str]:
            rlt = [text[idx : idx + leg] for idx in range(0, len(text), leg)]
            rlt.sort()
            return rlt
        def run():
            all_words_leg = len(''.join(words))
            if all_words_leg == 0:
                return []
            word_leg = len(words[0])
            #因為題目有說 words 內的 word 長度相等
            s_leg = len(s)
            words.sort()
            rlt = []
            for i in range(s_leg - all_words_leg + 1):
                spilt_str = s[i: i + all_words_leg]
                if spilt_str in is_check_ok:
                    rlt.append(i)
                    continue
                elif spilt_str in is_check_no:
                    continue
                split_str_list = split_list(spilt_str, word_leg)
                if split_str_list == words:
                    #因為排序過了, 如果相等代表是所求的東西
                    rlt.append(i)
                    is_check_ok.add(spilt_str)
                else:
                    is_check_no.add(spilt_str)
            return rlt
        return run()
```
### 想法 3
再來這個方法是參考網路上的做法，可以使用 **滑動視窗** 的方式有效率地在字串中尋找匹配的子字串，避免了不必要的重複計算，具體步驟可以歸類以下
1. 在一個外層 for 中，從 0 到 word_leg - 1 的不同起始位置開始檢查，因為 **words**裡面每個子字串都相等
2. 在內層 for 中，以每次增加 word_leg 遍歷字串 s，並透過滑動視窗的方式，嘗試匹配包含 words 中所有單字的子字串
3. 對於每個單字 word，將其從 word_count(words 每個字串出現的次數) 字典中減去一個計數
4. 如果 word_count[word] 的值小於 0，表示目前視窗內某個單字已超過了在 **words** 中的數量，則需要往前找。 在這種情況下，for 會一直移動視窗的左側，同時將左側單字的計數加回，直到視窗內的單字數量符合 words 清單中的數量。
### 參考解法 3
```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_leg = len(words[0])
        # 因為題目有說 words 內的 word 長度相等
        all_words_leg = word_leg * len(words)
        rlt = []
        org_word_count = Counter(words)
        # 產生所有字串的數量
        
        for i in range(word_leg):
            start = i
            word_count = Counter(org_word_count)
            # 複製一份出來
            
            for j in range(i, len(s) - word_leg + 1, word_leg):
                word = s[j: j + word_leg]
                word_count[word] -= 1
                
                while word_count[word] < 0:
                    # 如果字串出現超過指定的數目
                    word_count[s[start: start + word_leg]] += 1
                    # 將前面的字串拿掉一直到符合
                    start += word_leg
                    # 開始位子也往前
                if start + all_words_leg == j + word_leg:
                    rlt. append(start)
        
        return rlt
```
### 參考想法 4
再來這個想法也和 **參考想法3**類似，只是他的計數器是加的，加到和 word_count(words 每個字串出現的次數) 相同，才是尋找的字串，且多 **words_used** 變數用來判斷是不是和尋找的 **words**字串相等(即所求字串)，來避免多餘的處理
### 解法 4
```python
class Solution:
	def findSubstring(self, s: str, words: List[str]) -> List[int]:
		word_leg = len(words[0])
		word_count = Counter(words)
		rlt = []

		for i in range(word_leg):
			start = i
			# 起始窗口位子
			window = defaultdict(int)
			# 用來存出現過的字串
			words_used = 0
			# 用來記錄找到的字串數目

			for j in range(i, len(s) - word_leg + 1, word_leg):
				word = s[j:j + word_leg]

				if word not in word_count:
					# 如果現在這斷字串不在要找的目標中
					start = j + word_leg
					# 往下一段字串找並初始其他變數
					window = defaultdict(int)
					words_used = 0
					continue

				words_used += 1
				window[word] += 1

				while window[word] > word_count[word]:
					# 如果字串出現超過指定的數目
					window[s[start:start + word_leg]] -= 1
					# 將前面的字串拿掉一直到符合
					start += word_leg
					words_used -= 1

				if words_used == len(words):
					rlt.append(start)

		return rlt
```

參考:  
[✔️Python 90% with Detailed Explanation | sliding windows using Counter ^_^](https://leetcode.com/problems/substring-with-concatenation-of-all-words/solutions/2417727/python-90-with-detailed-explanation-sliding-windows-using-counter/)  
[Python Elegant & Short | Sliding window | 98.89% faster](https://leetcode.com/problems/substring-with-concatenation-of-all-words/solutions/2418859/python-elegant-short-sliding-window-98-89-faster/)  