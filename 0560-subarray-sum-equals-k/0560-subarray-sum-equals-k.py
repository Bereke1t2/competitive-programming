class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = s = 0
        dic = {0: 1} 
        for num in nums:
            s += num
            if (s - k) in dic:
                res += dic[s - k]
            dic[s] = dic.get(s, 0) + 1
        return res