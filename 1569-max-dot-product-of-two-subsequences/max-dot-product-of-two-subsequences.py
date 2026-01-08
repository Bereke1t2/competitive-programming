class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo  = defaultdict(int)
        n1 , n2 = len(nums1) , len(nums2)
        def dp(i , j):
            nonlocal memo
            if i>=n1 or j>=n2:
                return 0
            if (i , j) in memo:
                return memo[(i , j)]
            ans = max(nums1[i]*nums2[j] + dp(i+1 , j+1) , dp(i+1 , j) , dp(i , j+1))
            memo[(i,j)] = ans
            return ans
        
        ans = dp(0 , 0)
        min1_ , max_1 = min(nums1) , max(nums1)
        min2_ , max_2 = min(nums2) , max(nums2)
        if ans==0:
            return max(min1_*max_2 , min2_*max_1)
        return ans