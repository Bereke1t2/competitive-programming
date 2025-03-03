class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [0]*len(nums)
        index = 0
        for i in range(len(nums)):
            if nums[i]<pivot:
                res[index] = nums[i]
                index +=1
        for i in range(nums.count(pivot)):
            res[index] = pivot
            index +=1
        for i in range(len(nums)):
            if pivot<nums[i]:
                res[index] = nums[i]
                index +=1
        return res