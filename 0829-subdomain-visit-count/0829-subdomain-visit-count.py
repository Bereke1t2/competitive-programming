class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        d = defaultdict(int)

        for cpdomain in cpdomains:
            count , domains = cpdomain.split()
            domains = domains.split('.')
            for i in range(0,len(domains)):
                d['.'.join(domains[i:])] +=int(count)
        res = [str(count) +" "+ domain for domain , count in d.items()]
        return res


