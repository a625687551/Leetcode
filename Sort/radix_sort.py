# !/usr/bin/env python3
# -*- coding:utf-8 -*-


def select_sort(lists):
    # 直接排序
    count = len(lists)
    for i in range(count):
        min = i
        for j in range(i+1, count):
            if lists[min] > lists[j]:
                min = j
            lists[min], lists[i] = lists[i], lists[min]
    return lists


if __name__ == '__main__':
    l = [29, 10, 15, 37, 14]
    f = select_sort(l)
    print("finally {}".format(f))
