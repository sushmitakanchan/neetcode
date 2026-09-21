Given arrival arr[] and departure dep[] times of trains on the same day, find the minimum number of platforms needed so that no train waits. A platform cannot serve two trains at the same time; if a train arrives before another departs, an extra platform is needed.

Note: Time intervals are in the 24-hour format (HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0). Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).

Examples:

Input: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
Output: 3
Explanation: There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.
Input: arr[] = [900, 1235, 1100], dep[] = [1000, 1240, 1200]
Output: 1
Explanation: All train times are mutually exclusive. So we need only one platform.
Input: arr[] = [1000, 935, 1100], dep[] = [1200, 1240, 1130]
Output: 3
Explanation: All three trains have to be there from 11:00 to 11:30
Constraints:

1 ≤ arr.size(), dep.size() ≤ 105
0000 ≤ arr[i] ≤ dep
0000 ≤ dep[i] ≤ 2359


class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        # code here
        sortedArrival = sorted(arr)
        sortedDeparture = sorted(dep)
        
        if not arr:
            return 0
            
        arrival_index = 0
        departure_index = 0
        platforms_in_use = 0
        max_platforms = 0
        
        while arrival_index < len(sortedArrival):
            if sortedArrival[arrival_index] <= sortedDeparture[departure_index]:
                platforms_in_use += 1
                max_platforms = max(max_platforms, platforms_in_use)
                arrival_index += 1
            else:
                platforms_in_use -= 1
                departure_index += 1
        return max_platforms
        
        
