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
        # prev, current = None, head 
        # while current != None :
            
        #     current.next = prev 
        #     prev = current
        #     current = next 
        #     next = current.next 
        # head = prev  
        # return head

        currnode =  head 
        prev = None 
        while currnode is not None:
            currnode.next = prev 
            prev = currnode
            