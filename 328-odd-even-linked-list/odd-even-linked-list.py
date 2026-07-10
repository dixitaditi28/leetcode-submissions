# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odds = []
        evens = []

        curr = head
        isOdd = True
        while curr:
            if isOdd:
                odds.append(curr)
            else:
                evens.append(curr)
            isOdd = not isOdd
            curr = curr.next

        for i in range(len(odds)-1):
            odds[i].next = odds[i + 1]
        odds[-1].next = evens[0]

        for i in range(len(evens) - 1):
            evens[i].next = evens[i + 1]                 
        evens[-1].next = None
        return odds[0]      