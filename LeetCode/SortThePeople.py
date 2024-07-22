class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for i, name in sorted(enumerate(names), key=lambda tup: heights[tup[0]], reverse=True)]
