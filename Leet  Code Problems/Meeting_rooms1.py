#most impt problem 
# FB, Apple, Google, Microsoft, Amazon, Bloomberg, Uber, Yelp, Apple, Snapchat, Cisco
# Link : https://leetcode.com/problems/meeting-rooms/

# Given an array of meeting time intervals consisting 
# of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine 
# if a person could attend all meetings.

# For example,

# Given [[0, 30],[5, 10],[15, 20]],
# return false.
# input :  [[7,10],[2,4]]  
# return True

def meeting_rooms(intervals):
    intervals.sort()
    n = len(intervals)
    for i in (1,n):
        if intervals[i][0] < intervals[i-1][1]:
            return False 
        else :
            return True

arr =  [[7,10],[2,4]] 
arr1 = [[0, 30],[5, 10],[15, 20]] 

print(meeting_rooms(arr))
print(meeting_rooms(arr1))



