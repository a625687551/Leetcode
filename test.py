# coding: utf-8

# class Test(object):
#     name = 'python'
#     word = u"meta"
#
#
# a = Test()
# print(a.name)
# print(a.word)

import pandas as pd

str_list = "abc123efgaacddf444z"


def check_str(str_list):
    A = pd.DataFrame(list(str_list))
    A.columns = ['s']
    A["num"] = 0
    # 计算字符等值数目
    for index, rows in A[1:].iterrows():
        if rows["s"] == A.loc[(index - 1), "s"]:
            A.loc[index, "num"] = A.loc[(index - 1), "num"] + 1
        else:
            A.loc[index, "num"] = 0
    # 定位最长等值字符串，并打印
    max_index = A[A["num"] == max(A['num'])].index[0] + 1
    min_index = A[A["num"] == max(A['num'])].index[0] - max(A["num"])
    print(str_list[min_index:max_index])


if __name__ == '__main__':
    check_str(str_list)
