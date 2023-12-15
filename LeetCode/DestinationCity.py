# given there's exactly one destination city, just find one that appears in the list but never first in a pair
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations_that_are_not_sources = set()
        sources_that_are_not_destinations = set()
        for source, destination in paths:
            if source in destinations_that_are_not_sources:
                destinations_that_are_not_sources.remove(source)
            else:
                sources_that_are_not_destinations.add(source)
            if destination in sources_that_are_not_destinations:
                sources_that_are_not_destinations.remove(destination)
            else:
                destinations_that_are_not_sources.add(destination)
        assert len(destinations_that_are_not_sources) == 1
        return next(iter(destinations_that_are_not_sources))
