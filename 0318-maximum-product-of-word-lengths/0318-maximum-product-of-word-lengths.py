class Solution:
    def maxProduct(self, words: List[str]) -> int:
        nums = []
        for word in words:
            num = 0
            for l in word:
                num |=1<<(ord(l) - ord('a')+1)
            nums.append([num,len(word)])
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                num1 , len1 = nums[i]
                num2 , len2 = nums[j]
                if num1 & num2 == 0:
                    res = max(res,len1*len2)
        return res