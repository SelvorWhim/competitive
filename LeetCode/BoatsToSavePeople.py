class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        first_i = 0
        last_i = len(people) - 1
        boats = 0
        while first_i <= last_i:
            # if we can fit the next lightest together with the next heaviest, do that.
            # otherwise, only take the next heaviest (by assumption, they should fit).
            if people[first_i] + people[last_i] <= limit:
                first_i += 1
            last_i -= 1
            boats += 1
        return boats
