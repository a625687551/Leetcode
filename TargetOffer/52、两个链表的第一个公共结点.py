# -*- coding:utf-8 -*-
"""
输入两个链表，找出它们的第一个公共结点。
1.先遍历list 放到两个辅助栈中，每次弹出一个，对比，时间复杂度和空间复杂度是O(m+n)
2.先遍历list记住长度m n，长的先走几步对齐，然后在逐个对比，时间复杂度O(m+n)空间复杂度1
3、用两个指针扫描”两个链表“，最终两个指针到达 null 或者到达公共结点。不用记住长度
"""


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = pHead2 if not p1 else p1.next
            p2 = pHead1 if not p2 else p2.next

        return p1

if __name__ == '__main__':
    s = Solution()
    print(s.FindFirstCommonNode(2, 5))
