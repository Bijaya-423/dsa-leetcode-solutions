'''problem - count tested devices after test operations


you are given an array batteryPercentages where each element represents the battery percentage of a devide

Devices are tested from left to right:
- if a device had battery > 0, it is tested.
- each test reduces the battery of all future devices by 1(not below 0).
- count how manny devices are tested after all devices are tested.


approach:
instead of actually reducing future batteries,
keep track of how many devices have already been tested.
for each device, check if (battery - tested_count) > 0.



'''



from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0

        for battery in batteryPercentages:
            if battery - tested > 0:
                tested += 1
        
        return tested

#example
solution = Solution()
battery = [3, 2, 1, 4, 5]
print(solution.countTestedDevices(battery))  # Output: 4

solution = Solution()
battery = [0, 1, 2, 3, 4]
print(solution.countTestedDevices(battery))  # Output: 4
