class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        N = len(s)
        res = [0]*N
        
        for curr_index , index in enumerate(indices):
            res[index] = s[curr_index]

        return ''.join(res)
