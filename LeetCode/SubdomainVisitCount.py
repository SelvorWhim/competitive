from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        c = Counter()
        for counted_domain in cpdomains:
            count, domain = counted_domain.split()
            subs = domain.split('.')
            for i in range(len(subs)):
                c[".".join(subs[i:])] += int(count)
        return ["{} {}".format(c[sub], sub) for sub in c]
