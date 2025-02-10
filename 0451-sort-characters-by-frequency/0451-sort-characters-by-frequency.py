class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_dic = {}
        ans = ""
        for c in s:
            if c not in frequency_dic:
                frequency_dic[c]=s.count(c)
        frequency_dic = dict(sorted(frequency_dic.items(),key=lambda item:item[1],reverse=True))
        for f in frequency_dic.keys():
            ans += f*frequency_dic[f]
        return ans


        