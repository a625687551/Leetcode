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
"""


class Solution:
    """我在想这个用numpy是不是更好解决?"""

    def hasPath(self, matrix, rows, cols, path):
        if not matrix or not path or rows < 1 or cols < 1:
            return False
        for row in range(rows):
            for col in range(cols):
                if matrix[row * cols + col] == path[0]:
                    if self.find_way(list(matrix), rows, cols, path[1:], row, col):
                        return True
        return False

    def find_way(self, matrix, rows, cols, path, row, col):
        if not path:
            return True
        matrix[row * cols + col] = '0'
        if col + 1 < cols and matrix[row * cols + col + 1] == path[0]:
            return self.find_way(matrix, rows, cols, path[1:], row, col + 1)
        elif col - 1 >= 0 and matrix[row * cols + col - 1] == path[0]:
            return self.find_way(matrix, rows, cols, path[1:], row, col - 1)
        elif row + 1 < rows and matrix[(row + 1) * cols + col] == path[0]:
            return self.find_way(matrix, rows, cols, path[1:], row + 1, col)
        elif row - 1 >= 0 and matrix[(row - 1) * cols + col] == path[0]:
            return self.find_way(matrix, rows, cols, path[1:], row - 1, col)
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SLHECCEIDEJFGGFIE"))
