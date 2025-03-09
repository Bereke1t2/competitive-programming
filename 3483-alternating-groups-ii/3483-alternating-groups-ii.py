class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        left , right = 0, 0
        count = 0
        colors.extend(colors[:k])
        while right<len(colors)-1:
            if right - left +1==k:
                count +=1
                left +=1
            elif colors[right]!=colors[right+1]:
                right +=1
            else:
                left = right +1
                right = left
        return count
        [0,0,0,1,0,0,0]

        