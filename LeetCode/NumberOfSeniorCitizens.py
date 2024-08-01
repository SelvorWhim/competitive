def is_senior(passenger):
    return int(passenger[11:13]) > 60

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for passenger in details if is_senior(passenger))
