class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = {num for num in nums}
        def backtrack(i,curr):
            if i == len(curr):
                return None if ''.join(curr) in seen else ''.join(curr)
            
            res = backtrack(i+1,curr)
            if res:return res

            curr[i] = '1'
            return backtrack(i+1,curr)
        return backtrack(0,['0' for _ in range(len(nums[0]))])

