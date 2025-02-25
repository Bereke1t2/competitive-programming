class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        store = {}
        for index , num in enumerate(nums):
            total +=num
            if total%k==0 and index!=0:
                return True
            elif total%k in store:
                if index-store[total%k]>1:
                    return True
            else:
                store[total%k]=index
        return False        