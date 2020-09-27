# idea: Convert each interval into 2 points, one adding passengers and one removing, go through list and see if it ever goes over capacity.

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_points = []
        for trip in trips:
            trip_points.append((trip[1], trip[0])) # +num_passengers at start_location
            trip_points.append((trip[2], -trip[0])) # -num_passengers at end_location
        trip_points.sort() # tuple default sort is by first element, so by start/end location
        curr_capacity = 0
        for trip_point in trip_points:
            curr_capacity += trip_point[1]
            if curr_capacity > capacity:
                return False
        return True
