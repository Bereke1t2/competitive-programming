class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        nums = [3**i for i in range(16)]
        index = 0
        while nums[index]<=n:
            index +=1
        for i in range(index -1 , -1,-1):
            if n >= nums[i]:
                n -=nums[i]
            if n==0:
                return True
        # print(n)
        return n==0


