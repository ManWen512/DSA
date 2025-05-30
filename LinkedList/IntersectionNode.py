# Definition for singly-linked list.
# class ListNode:
# def init(self, x):
# self.val = x
# self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        while headA:
            setA.add(headA)
            headA = headA.next

        while headB:
            if headB in setA:
                return headB
            headB = headB.next

        return None
