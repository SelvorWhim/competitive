import heapq

# use dict mapping label to set of use_limit largest items with that label.
# take the num_wanted largest values among all these sets (or less, if there aren't enough total)
# can use a min heap for each label's set, removing min whenever it grows above use_limit
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        heaps = {}
        for i in range(len(values)): # assuming values and labales lists are same length
            if labels[i] not in heaps.keys():
                heaps[labels[i]] = []
            heapq.heappush(heaps[labels[i]], values[i])
            if len(heaps[labels[i]]) > use_limit:
                heapq.heappop(heaps[labels[i]]) # remove min. Maintain only use_limit top elements for each label
        return sum(sorted([value for heap in heaps.values() for value in heap], reverse = True)[:num_wanted])
