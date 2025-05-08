class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index = 0 - 1
        i = 0
        while i<len(nums):
            if nums[i]+index!=i:
                num = nums[i]
                if nums[i]+index<0 or nums[i]+index>=len(nums) or nums[i] == nums[num+ index]:
                    i+=1
                else:
                    nums[i] , nums[num+ index] = nums[num + index] , nums[i]
            else:
                i +=1
        target = 1
        for num in nums:
            if num==target:
                target +=1
            else:
                return target
        return target


