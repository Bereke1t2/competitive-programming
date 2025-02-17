class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        store = {0:1}
        count = 0
        for num in nums:
            total +=num
            rem = total%k

            if rem in store:
                count +=store[rem]
                store[rem] +=1
            else:
                store[rem] = 1
        return count