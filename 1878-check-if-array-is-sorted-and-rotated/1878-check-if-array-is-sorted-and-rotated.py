class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 1 
        N  = len(nums)
        for i in range (2*N-1):
            if nums[i%N] <= nums[(i+1)%N]:
                count +=1
            else:
                count = 1
            if count == N:
                return True
        return N==1