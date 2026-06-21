class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_num = max(costs)
        count = [0]*(max_num+1)
        for cost in costs:
            count[cost] +=1
        max_ic = 0
        falge =  False
        for i in range(max_num+1):
            while count[i]:
                coins -=i
                count[i] -=1
                if coins<0:
                    falge = True
                    break
                max_ic +=1
            if falge:
                break
        return max_ic
