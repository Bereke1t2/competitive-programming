class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        for length in range(len(nums),1 , -1):
            left  = 0
            even = Counter()
            odd = Counter()
            for right in range(len(nums)):
                if nums[right]%2==0:
                    even[nums[right]] +=1
                else:
                    odd[nums[right]] +=1
                if right - left +1 == length:
                    if len(even) == len(odd):
                        return length
                    if nums[left]%2==0:
                        even[nums[left]] -=1
                    else:
                        odd[nums[left]] -=1
                    if not even[nums[left]]: del even[nums[left]]
                    if not odd[nums[left]]: del odd[nums[left]]
                    left +=1
        return 0                    
