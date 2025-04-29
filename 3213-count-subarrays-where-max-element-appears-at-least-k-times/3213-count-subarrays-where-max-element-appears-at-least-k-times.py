class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        max_ = max(nums)
        frq = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            num = nums[right]
            frq[num] +=1
            while frq[max_]>=k:
                frq[nums[left]] -=1
                left +=1
            count +=left
        return count