class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans_index = 0
        if sum(gas) < sum(cost):
            return -1
        Sum = 0
        for i in range(len(gas)):
            Sum +=gas[i] - cost[i]
            
            if Sum<0:
                Sum = 0
                ans_index = i+1
        return ans_index
