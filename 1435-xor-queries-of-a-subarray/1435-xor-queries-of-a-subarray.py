class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        xor = 0
        for num in arr:
            xor ^=num
            prefix_xor.append(xor)
        res = []
        for left , right  in queries:
            ans = 0
            ans ^=prefix_xor[left]
            ans ^=prefix_xor[right+1]
            res.append(ans)
        return res