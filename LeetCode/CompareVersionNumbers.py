def version_str_to_int_arr(version):
    return [int(ns) for ns in version.split('.')]

def compare_version_int_arr(v1, v2):
    n1 = len(v1)
    n2 = len(v2)
    if n1 < n2:
        v1 += (n2-n1)*[0]
    elif n2 < n1:
        v2 += (n1-n2)*[0]
    for i in range(max(n1,n2)):
        if v1[i] < v2[i]:
            return -1
        elif v1[i] > v2[i]:
            return 1
    return 0

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        return compare_version_int_arr(version_str_to_int_arr(version1), version_str_to_int_arr(version2))
