#FB, Apple, Google, Microsoft 
#most asked FB
# Link : https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

#SOLN : 
class LL:
    def __init__(self):
        self.head = None 
    
    def append (self,data) :
        newnode = ListNode(data, None)
        # print(newnode.val)
        if self.head == None :
            self.head = newnode 
            return 
        lastnode = self.head 
        # print(self.head.val)
        while lastnode.next :
            lastnode = lastnode.next 
        lastnode.next = newnode
        
    def print(self):
        
        return self.head

        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr = []
        for items in lists:
            # head = items.val
            while items:
                arr.append(items.val)
                items = items.next
        arr.sort()
        a = LL()
        for i in arr :
            a.append(i)
        # a.append(arr[0])
        # a.append(arr[1])
        return a.print()

# --------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None 
        
# class LL:
#     def __init__(self):
#         self.head = None
#     def append_to_list(self,data):
        
#         newnode = node(data)
#         print(newnode.data)
#         if self.head == None:
#             self.head = newnode
#         # print(self.head.data)
#         # # print(newnode.data)
#         lastnode = self.head
#         while lastnode.next:
#             lastnode = lastnode.next
#         lastnode.next = newnode

        
        
        
        
            
        
         