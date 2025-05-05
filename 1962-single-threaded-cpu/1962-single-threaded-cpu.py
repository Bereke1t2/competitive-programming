class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = [(p[0], k , p[1]) for k ,p in enumerate(tasks)]
        tasks.sort(key=lambda item:(item[0] , item[2]))
    
        heap = [tasks[0][::-1]]
        start = 1
        res = []
        total = tasks[0][0]
        def add():
            nonlocal start , total , tasks ,  heap
            for i in range(start,n):
                if tasks[i][0]<=total:
                    heappush(heap , tasks[i][::-1])
                else:
                    start = i 
                    break
            else:
                start  = n+1

        while heap:
            time , index , _ = heappop(heap)
            total +=time
            res.append(index)
            add()
            if len(heap)==0 and len(res)!=n:
                total = tasks[start][0]
                add()

        return res