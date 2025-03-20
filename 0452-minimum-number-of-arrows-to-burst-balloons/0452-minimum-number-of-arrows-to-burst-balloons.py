class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        nums = []
        count = 0
        bursted = set()

        for index , point in enumerate(points):
            start , end  = point
            nums.append([start,1,index])
            nums.append([end,-1,index])
        
        nums.sort(key=lambda item:(item[0],-item[1]))
        stack = []
        for point , check , index in nums:
            if check==-1 and index not in bursted:
                count +=1
                while stack:
                    bursted.add(stack.pop())
                bursted.add(index)
                continue
            if index in bursted:continue
            stack.append(index)
        return count

