class Solution:
    def smallestNumber(self, pattern: str) -> str:
        for check in ["".join(p) for p in permutations('123456789')]:
            for i in range(len(pattern)):
                if pattern[i]=='I':
                    if check[i]>=check[i+1]:
                        break
                else:
                    if check[i] <= check[i+1]:
                        break
            else:
                return check[:len(pattern)+1]

