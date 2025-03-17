class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course1 , course2 in prerequisites:
            graph[course1].append(course2)
        memo = defaultdict(int)
        def dfs(i,path):
            if i in path:
                return False
            if not graph[i]:
                return True
            if memo[i]:
                return 1==memo[i]
            check = True
            path.add(i)
            for j in graph[i]:
                check = check and dfs(j , path)
            path.remove(i)
            memo[i] = -1 if check==False else 1
            return memo[i]==1

        check = True
        for i in range(numCourses):
            check = check and dfs(i , set())
        return check
            
        