# -*- coding:utf-8 -*-
"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
.此时慢指针走的路程为Sslow = x + m * c + a
快指针走的路程为Sfast = x + n * c + a
2 Sslow = Sfast
2 * ( x + m*c + a ) = (x + n *c + a)
从而可以推导出：
x = (n - 2 * m )*c - a
= (n - 2 *m -1 )*c + c - a
即环前面的路程 = 数个环的长度（为可能为0） + c - a
什么是c - a？这是相遇点后，环后面部分的路程。（橙色路程）
所以，我们可以让一个指针从起点A开始走，让一个指针从相遇点B开始继续往后走，
2个指针速度一样，那么，当从原点的指针走到环入口点的时候（此时刚好走了x）
从相遇点开始走的那个指针也一定刚好到达环入口点。
所以2者会相遇，且恰好相遇在环的入口点。
最后，判断是否有环，且找环的算法复杂度为：
时间复杂度：O(n)
空间复杂度：O(1)
"""


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return None
        fast = pHead.next.next
        slow = pHead.next
        while fast != slow:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    s = Solution()
    print(s.EntryNodeOfLoop([1,3]))
