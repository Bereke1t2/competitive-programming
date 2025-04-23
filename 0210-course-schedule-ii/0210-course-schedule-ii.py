class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        graph = defaultdict(list)

        for c1 , c2 in prerequisites:
            graph[c2].append(c1)
            indegree[c1] +=1
        
        q = deque()
        for c in range(numCourses):
            if not indegree[c]:
                q.append(c)
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for d in graph[c]:
                indegree[d] -=1
                if not indegree[d]:
                    q.append(d)
        return res if sum(indegree)==0 else []



