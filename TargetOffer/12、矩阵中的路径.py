# -*- coding:utf-8 -*-
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如这样的3 X 4 矩阵中包含一条字符串"bfce"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
a b t g 
c f c s 
j d e h 
回溯法来解决
动态规划
"""


class Solution:
    """我在想这个用numpy是不是更好解决?"""

    def hasPath(self, matrix, path):
        if not matrix or not path:
            return -1
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == path[0]:
                    if self.find_way(matrix, row, col, path[1:]):
                        return True
        return False

    def find_way(self, matrix, row, col, path):
        if not path:
                return True
        rows, cols = len(matrix), len(matrix[0])
        matrix[row][col] = 0
        if col + 1 < cols and matrix[row][col + 1] == path[0]:
            return self.find_way(matrix, row, col + 1, path[1:])
        elif col - 1 >= 0 and matrix[row][col - 1] == path[0]:
            return self.find_way(matrix, row, col - 1, path[1:])
        elif row + 1 < rows and matrix[row + 1][col] == path[0]:
            return self.find_way(matrix, row + 1, col, path[1:])
        elif row - 1 >= 0 and matrix[row - 1][col] == path[0]:
            return self.find_way(matrix, row - 1, col, path[1:])
        else:
            return False

    def has_path(self):
        pass


if __name__ == '__main__':
    matrix = [['A', 'B', 'C', 'E', 'H', 'J', 'I', 'G'],
              ['S', 'F', 'C', 'S', 'L', 'O', 'P', 'Q'],
              ['A', 'D', 'E', 'E', 'M', 'N', 'O', 'E'],
              ['A', 'D', 'I', 'D', 'E', 'J', 'F', 'M'],
              ['V', 'C', 'E', 'I', 'F', 'G', 'G', 'S']]
    way = ['S', 'L', 'H', 'E', 'C', 'C', 'E', 'I', 'D', 'E', 'J', 'F', 'G', 'G', 'F', 'I', 'E']
    s = Solution()
    print(s.hasPath(matrix, way))
