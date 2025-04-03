class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i <len(nums):
            if nums[i]!=i+1:
                if nums[nums[i]-1]==nums[i]:
                    i+=1
                    continue
                pos = nums[i] -1
                nums[i] ,nums[pos] = nums[pos] , nums[i]
            else:
                i+=1
        ans = []
        for i in range(len(nums)):
            if nums[i]!= i+1:
                ans.append(i+1)
        return ans