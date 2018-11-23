# coding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def solution_over(self, head1,head2):
        if not head1 and not head2:
            return None
        if not head1 and head2:
            return head2
        if not head2 and head1:
            return head1
        p1, p2 = head1, head2
        p = ListNode
        r = p
        while p1 and p2:
            if p1.val >= p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        return r.next




if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    print(s.solution_over(2, -5))
