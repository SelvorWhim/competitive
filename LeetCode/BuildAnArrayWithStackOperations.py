# idea: push any element in sequence 1,2,3...n that appears in output, push+pop any intermediate that doesn't
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ret = []
        i_target = 0
        n_target = len(target)
        for i in range(1, n+1):
            ret.append('Push')
            if i < target[i_target]:
                ret.append('Pop')
            else:
                i_target += 1
                if i_target >= n_target:
                    break
        return ret
