class Solution:
    def topKFrequent(self, A, k):

        res = list(sorted(Counter(A).items(), key=lambda x: [-x[1], x[0]]))
        return [res[i][0] for i in range(k)]