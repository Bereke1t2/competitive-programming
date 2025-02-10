class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = list(zip(names,heights))
        temp.sort(key=lambda item:item[1] , reverse=True)
        return [name for name, _ in temp]
        for Pass in range(len(names)):
            swap = False
            for index in range(len(names)-Pass-1):
                if heights[index]<heights[index+1]:
                    swap = True
                    heights[index] , heights[index+1] = heights[index+1] , heights[index]
                    names[index] , names[index+1] = names[index+1] , names[index]
            if not swap:
                break
        return names