# Use two pointers:

# pointerA → start from headA

# pointerB → start from headB

# Move both one step at a time.

# When a pointer reaches end → move it to the other list's head.

# Eventually:

# They will meet at intersection node

# Or both become None










from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA


# -------------------------
# Example Test (VS Code)
# -------------------------

if __name__ == "__main__":

    # Create intersecting part
    intersect = ListNode(8)
    intersect.next = ListNode(4)
    intersect.next.next = ListNode(5)

    # List A
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersect

    # List B
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersect

    solution = Solution()
    result = solution.getIntersectionNode(headA, headB)

    if result:
        print("Intersected at:", result.val)
    else:
        print("No intersection")
