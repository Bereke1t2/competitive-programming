class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        freq_p = defaultdict(int)
        freq_p[0] = 1
        prefix = 0
        index = nums.index(k)
        for i in range(index-1,-1 , -1):
            prefix += (1 if nums[i]>k else -1)
            freq_p[prefix] +=1
        count = freq_p[1] + freq_p[0]

        prefix = 0
        for i in range(index + 1, len(nums)):
            prefix += (1 if nums[i]>k else -1)
            count +=freq_p[1-prefix]
            count +=freq_p[-prefix]
        return count 


        

        