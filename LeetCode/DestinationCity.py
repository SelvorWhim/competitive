# given there's exactly one destination city, just find one that appears in the list but never first in a pair
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        not_destination = set() # cities with outgoing paths
        destination_candidate = set()
        for from_city, to_city in paths:
            not_destination.add(from_city)
            destination_candidate.discard(from_city)
            if to_city not in not_destination:
                destination_candidate.add(to_city)
        return destination_candidate.pop() # by assumption, there should be exactly one
