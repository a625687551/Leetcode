# -*- coding:utf-8 -*-

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，
那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义 : ) 。
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        return self.judge(sequence, 0, len(sequence) - 1)

    def judge(self, seq, left, right):
        """
        :nums: 后续遍历序列
        :left: 起点
        :right: 终点(二叉树及其子树的根节点)
        :return:
        """
        if left > right:
            return True
        index = left
        while (index < right) and (seq[index] < seq[right]):
            index += 1
        root_index = index
        while index < right:
            if seq[index] < seq[right]:
                return False
            index += 1
        return self.judge(seq, left, root_index - 1) and self.judge(seq, root_index, right - 1)
