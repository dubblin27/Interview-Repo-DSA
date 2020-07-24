'''
Google, FB, Amazon 
Link : https://leetcode.com/problems/reverse-linked-list/ 

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Input: NULL
Output: NULL

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None 
        currentnode = head 
        # 1-2-3-None 
        # currnode = 1 
        while currentnode != None :
            next = currentnode.next 
            #next = 2
            currentnode.next = previous
            #1->None
            previous = currentnode
            #prev = 1
            currentnode = next
            #currnode = 2

            # next = 3
            # 2->1->None 
            # prev = 2
            # currentnode = 3

            # next = None
            # 3->2->1->None 
            # prev = 3
            # currentnode = None 

            # break 
        head = previous
        return head




        