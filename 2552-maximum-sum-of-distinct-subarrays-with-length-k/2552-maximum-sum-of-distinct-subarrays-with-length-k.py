class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        Sum = max_ = 0
        d = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            Sum +=nums[right]
            d[nums[right]] +=1
            while right - left + 1 > k:
                Sum -=nums[left]
                d[nums[left]] -=1
                if not d[nums[left]]:
                    del d[nums[left]]
                left +=1
            if right - left + 1 == len(d) and len(d)==k:
                max_ = max(max_ , Sum)
        return max_