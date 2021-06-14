class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda tup: tup[1], reverse=True)
        total_fit = 0
        for num, units in boxTypes:
            boxes_fit = min(num, truckSize)
            total_fit += boxes_fit * units
            truckSize -= boxes_fit
            if truckSize <= 0: # shouldn't be less
                break
        return total_fit
