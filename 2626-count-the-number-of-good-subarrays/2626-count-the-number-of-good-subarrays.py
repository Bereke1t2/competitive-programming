class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        num_sub = 0
        count = 0
        d = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            d[nums[right]] +=1
            if d[nums[right]]>1:
                count +=d[nums[right]]
                count -=1
            while count>=k:
                num_sub += (len(nums) - right)
                d[nums[left]] -=1
                count -=d[nums[left]]
                left +=1
        return num_sub
