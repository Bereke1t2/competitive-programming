class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ns = [0]
        ys = [0]
        for l in customers:
            if l=='Y':
                ys.append(ys[-1]+1)
                ns.append(ns[-1])
            else:
                ys.append(ys[-1])
                ns.append(ns[-1]+1)
        best = float('-inf')
        for i in range(len(customers) + 1):
            local = 2*(ys[i] - ns[i])  + ns[-1] - ys[-1]
            if local>best:
                index = i
                best = local
        return index

        