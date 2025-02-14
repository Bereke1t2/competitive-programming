class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        search = Counter({key:val-len(s)//4 for key , val in count.items() if val>len(s)//4})

        min_len = 2*len(s)
        left  = 0
        check = Counter()
        def test(t1,t2):
            if not t1:return False
            for key in t1:
                if t1[key]>t2[key]:
                    return False
            return True
        for right in range(len(s)):
            check[s[right]] +=1
            while test(search,check) and left <= right:
                print(left,right)
                min_len = min(min_len,right-left +1)
                check[s[left]] -=1
                if not check[s[left]]:
                    del check[s[left]]
                left +=1
        return min_len if min_len !=2*len(s) else 0