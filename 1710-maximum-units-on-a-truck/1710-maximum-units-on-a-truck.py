class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #sort by units per box descending
        boxTypes.sort(key = lambda x : x[1], reverse=True)

        total_units = 0

        for boxes, units in boxTypes:
            take = min(boxes, truckSize)

            total_units += take * units

            truckSize -= take

            if truckSize == 0:
                break
        return total_units

