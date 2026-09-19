## Meeting Rooms

**Difficulty:** Easy
**Topic:** Arrays, sorting, intervals
**Original problem:** [LeetCode 252 — Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

### Problem

You are given a list of meeting time intervals. Each interval is represented as `[start, end]`.

Determine whether **one person can attend every meeting**. Return `False` if any meetings overlap; otherwise, return `True`.

A meeting that starts exactly when another meeting ends does **not** overlap.

### Examples

**Example 1**

```python
Input:  [[0, 30], [5, 10], [15, 20]]
Output: False
```

The meeting from `0` to `30` overlaps with the other meetings.

**Example 2**

```python
Input:  [[7, 10], [10, 12]]
Output: True
```

The second meeting starts exactly when the first ends, so the person can attend both.

**Example 3**

```python
Input:  [[13, 14], [9, 11], [10, 12]]
Output: False
```

The meetings `[9, 11]` and `[10, 12]` overlap. The input may be in any order.

### Function signature

```python
def can_attend_meetings(intervals):
    pass
```

SOLUTION:
def can_attend_meetings(intervals):
    sortedMeetings = sorted(intervals, key=lambda meeting: meeting[0])

    for i in range(1, len(sortedMeetings)):
        previous_end = sortedMeetings[i - 1][1]
        current_start = sortedMeetings[i][0]

        if current_start < previous_end:
            return False

    return True
      


intervals = [[13, 14], [9, 11], [10, 12]]
intervals1 = [[9, 10], [11, 12]]
print(can_attend_meetings(intervals1))

 “I sort the meetings by start time. Then I compare each meeting’s start with the 
previous meeting’s end. If it starts before the previous meeting ends, they overlap, s
o I return False. If I finish checking all meetings, I return True. 
Meetings that touch at the same time are allowed, which is why I use < rather than <=.”

Complexity:

Time: \(O(n \log n)\) — sorting dominates the \(O(n)\) scan.
Extra space: \(O(n)\) — sorted() creates a new list of \(n\) meetings.

For an empty list or one meeting, the loop does not run and the function correctly returns True.
