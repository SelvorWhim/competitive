# day 1 solution
# part 1: num_rises_1(parse_input(<input file contents>))
# part 2: num_rises_2(parse_input(<input file contents>))

from typing import List

def parse_input(input: str) -> List[int]:
    return [int(num_str) for num_str in input.split()]

def num_rises_1(nums: List[int]) -> int:
    return sum(nums[i] < nums[i+1] for i in range(len(nums) - 1))

def num_rises_2(nums: List[int]) -> int:
    # n1+n2+n3 < n2+n3+n4 -> n1 < n4
    return sum(nums[i] < nums[i+3] for i in range(len(nums) - 3))
