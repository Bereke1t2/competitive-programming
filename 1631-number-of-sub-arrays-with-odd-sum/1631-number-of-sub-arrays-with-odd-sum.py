class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        d = {0:1,1:0}
        Sum = count = 0
        for num in arr:
            Sum +=num
            count +=d[1-(Sum%2)]
            d[Sum%2] +=1
        return count%(10**9 + 7)