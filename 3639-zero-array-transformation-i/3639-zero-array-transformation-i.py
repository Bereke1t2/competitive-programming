class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff_array = [0]*len(nums)

        for left , right in queries:
            diff_array[left] -=1
            if right+1<len(nums):
                diff_array[right +1] +=1
        ps = []
        Sum = 0
        for num in diff_array:
            Sum +=num
            ps.append(Sum)
        for i in range(len(nums)):
            nums[i] +=ps[i]
            if nums[i]>0:
                return False
        return True
        