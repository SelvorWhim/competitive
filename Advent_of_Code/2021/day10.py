# day 10 solution
# part 1: syntax_error_score(parse_input(<input file contents>))
# part 2: completion_score(parse_input(<input file contents>))

from typing import List
from statistics import median

def parse_input(input: str) -> List[str]:
    return [line for line in input.split('\n')]

bracket_match_and_score = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137)
}

def syntax_error_score_line(line: str) -> int:
    stack = []
    for bracket in line:
        if bracket in bracket_match_and_score.keys():
            if bracket_match_and_score[bracket][0] != stack.pop(-1):
                return bracket_match_and_score[bracket][1]
        else:
            stack.append(bracket)
    return 0
    

def syntax_error_score(lines: List[str]) -> int:
    return sum(syntax_error_score_line(line) for line in lines)

bracket_match = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

bracket_score = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def completion_score_line(line: str) -> int:
    stack = []
    for bracket in line:
        if bracket in bracket_match.values():
            stack.append(bracket)
        else:
            if not stack or bracket_match[bracket] != stack.pop(-1):
                return 0
    score = 0
    for bracket in stack[::-1]: # reverse for order of completion string
        score *= 5
        score += bracket_score[bracket]
    return score

def completion_score(lines: List[str]) -> int:
    return median(filter(lambda score: score > 0, (completion_score_line(line) for line in lines)))
