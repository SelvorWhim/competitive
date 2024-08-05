class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen_once = set()
        seen_twice = set()
        for s in arr:
            if s not in seen_once:
                seen_once.add(s)
            elif s not in seen_twice:
                seen_twice.add(s)
        distinct_count = 0
        for s in arr:
            if s not in seen_twice:
                distinct_count += 1
                if distinct_count == k:
                    return s
        return ""
