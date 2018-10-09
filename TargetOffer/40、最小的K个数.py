# -*- coding:utf-8 -*-
import heapq


class Solution:
    def GetLeastNumbers_Solution_min(self, tinput, k):
        # 这个用最小堆
        if k <= 0 or not tinput or k > len(tinput):
            return []
        heapq.heapify(tinput)
        return [heapq.heappop(tinput) for _ in range(k)]

    def GetLeastNumbers_Solution_max(self, tinput, k):
        # 模拟最大堆,但是输出顺序貌似不对，这里可能有问题
        if k <= 0 or not tinput or k > len(tinput):
            return []
        max_heap = []
        for x in tinput:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -x)
            elif max_heap[0] < -x:
                heapq.heappushpop(max_heap, -x)
            else:
                continue
        return [x for x in max_heap]


if __name__ == '__main__':
    s = Solution()
    print(s.GetLeastNumbers_Solution_max([4, 5, 1, 6, 2, 7, 3, 8], 4))
