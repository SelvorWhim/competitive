class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        last_n = arr[0] # given length >= 1
        last_delta = 0
        curr_turbulence = 1
        max_turbulence = 1
        for n in arr[1:]:
            if n == last_n:
                curr_turbulence = 1
                last_delta_zero = True
            elif n > last_n:
                if last_delta < 0:
                    curr_turbulence += 1
                else:
                    curr_turbulence = 2
                last_delta_zero = False
                last_delta_positive = True
            else:
                if last_delta > 0:
                    curr_turbulence += 1
                else:
                    curr_turbulence = 2
                last_delta_zero = False
                last_delta_positive = False
            max_turbulence = max(max_turbulence, curr_turbulence)
            last_delta = n - last_n
            last_n = n
        return max_turbulence
