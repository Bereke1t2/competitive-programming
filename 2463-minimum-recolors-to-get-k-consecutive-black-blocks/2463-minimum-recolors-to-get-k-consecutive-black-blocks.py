class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        left = 0
        min_= k
        for right in range(len(blocks)):
            count +=blocks[right] == 'W'
            if right - left +1==k:
                min_ = min(min_ , count)
                count -=blocks[left] == 'W'
                left +=1
        return min_