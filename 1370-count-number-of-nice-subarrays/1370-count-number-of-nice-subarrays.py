class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def get(k):
            if k<0:
                return 0
            Sum = count = left = 0
            for right in range(len(nums)):
                Sum +=nums[right]
                while Sum>k:
                    Sum -=nums[left]
                    left +=1
                count += right - left +1
            return count


        nums = [num%2 for num in nums]
        
        return get(k) - get(k-1)

        