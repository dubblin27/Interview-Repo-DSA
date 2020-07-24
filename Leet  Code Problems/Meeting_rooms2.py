#most impt problem 
# FB, Apple, Google, Microsoft, Amazon, Bloomberg, Uber, Yelp, Apple, Snapchat, Cisco
# Leetcode 253 : https://leetcode.com/problems/meeting-rooms-ii/

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example, Given [[0, 30],[5, 10],[15, 20]], return 2.

from heapq import * 
def meeting_rooms(intervals):
    intervals.sort()
    rooms = 0 
    meetings = []

    for interval in intervals :
        if not meetings :
            meetings.append(interval[1])
            rooms +=1 
        else :
            if interval[0] >= meetings[0]:
                heappushpop(meetings,interval[1])
            else :
                heappush(meetings,interval[1])
                rooms +=1 
    return rooms


arr =  [[7,10],[2,4]]  
arr1 = [[0, 30],[5, 10],[15, 20]] 

print(meeting_rooms(arr))
# print(meeting_rooms(arr1))