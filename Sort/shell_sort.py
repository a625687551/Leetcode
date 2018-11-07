# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
希尔排序是插入排序的一种，是插入排序的一种高效改进算法，是非稳定的派逊
'''


def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = int(count / step)
    while group > 0:
        for i in range(group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists


if __name__ == '__main__':
    l = [29, 10, 14, 37, 14]
    f = shell_sort(l)
    print("finally {}".format(f))
