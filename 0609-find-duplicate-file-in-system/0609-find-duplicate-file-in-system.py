class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for path in paths:
            arr = path.split()
            for i in range(1,len(arr)):
                File = arr[i]
                index = File.index('(')
                store[File[index+1:-1]].append(arr[0]+"/"+File[:index])

        res = [path for path in list(store.values()) if len(path)>1]
        return res
