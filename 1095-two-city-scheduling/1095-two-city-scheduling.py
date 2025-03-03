class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda item:item[0] - item[1])
        n = len(costs)
        Sum = 0
        for i in range(n):
            if i<n//2:
                Sum +=costs[i][0]
            else:
                Sum +=costs[i][1]
        return Sum