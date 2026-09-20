Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104


Solution:
def merge(intervals):
        sortedIntervals = sorted(intervals, key = lambda interval:interval[0])
        merged=[]
  
        for start,end in sortedIntervals:
          if not merged or start > merged[-1][1]:
            merged.append([start, end])
          else:
            merged[-1][1] = max(merged[-1][1], end)

        return merged


I sort the intervals by start time, then scan them once, merging overlaps into the result. 
That takes \(O(n \log n)\) time and \(O(n)\) extra space.”
