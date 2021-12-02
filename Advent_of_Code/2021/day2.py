# day 2 solution
# part 1: product_of_navigation_1(parse_input(<input file contents>))
# part 2: product_of_navigation_2(parse_input(<input file contents>))

from typing import List

def parse_input(input: str) -> List[str]:
    return [step for step in input.split('\n')]

def product_of_navigation_1(steps: List[str]) -> int:
    horizontal = 0
    depth = 0
    for step in steps:
        direction, distance = step.split()
        distance = int(distance)
        if direction == 'forward':
            horizontal += distance
        elif direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance
        else:
            raise ValueError('unexpected direction')
    return horizontal * depth

def product_of_navigation_2(steps: List[str]) -> int:
    horizontal = 0
    aim = 0
    depth = 0
    for step in steps:
        direction, distance = step.split()
        distance = int(distance)
        if direction == 'forward':
            horizontal += distance
            depth += aim * distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
        else:
            raise ValueError('unexpected direction')
    return horizontal * depth
